using Google.Cloud.AutoML.V1;
using Google.Protobuf;
using System;
using System.IO;

public class AutoMLPredict
{
    public static void Main(string[] args)
    {
        string projectId = "your_project_id";
        string modelId = "your_model_id";
        string filePath = "path_to_your_image.jpg";

        PredictionServiceClient client = PredictionServiceClient.Create();
        ModelName modelName = ModelName.FromProjectLocationModel(projectId, "us-central1", modelId);

        ByteString content = ByteString.CopyFrom(File.ReadAllBytes(filePath));
        var payload = new ExamplePayload { Image = new Image { ImageBytes = content } };

        var response = client.Predict(modelName, payload);
        foreach (var annotationPayload in response.Payload)
        {
            Console.WriteLine($"Predicted label: {annotationPayload.DisplayName}, Confidence: {annotationPayload.Classification.Score}");
        }
    }
}
