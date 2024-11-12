public class GoogleCloudAutoML {

import com.google.cloud.automl.v1.AutoMlClient;
import com.google.cloud.automl.v1.PredictRequest;
import com.google.cloud.automl.v1.PredictionServiceClient;
import com.google.cloud.automl.v1.ModelName;
import com.google.cloud.automl.v1.ExamplePayload;
import com.google.protobuf.ByteString;
import java.nio.file.Files;
import java.nio.file.Paths;

public class AutoMLPredict {
    public static void main(String[] args) throws Exception {
        String projectId = "your_project_id";
        String modelId = "your_model_id";
        String filePath = "path_to_your_image.jpg";

        try (PredictionServiceClient client = PredictionServiceClient.create()) {
            ModelName modelName = ModelName.of(projectId, "us-central1", modelId);
            ByteString content = ByteString.copyFrom(Files.readAllBytes(Paths.get(filePath)));
            ExamplePayload payload = ExamplePayload.newBuilder().setImage(image).build();

            PredictRequest request = PredictRequest.newBuilder()
                    .setName(modelName.toString())
                    .setPayload(payload)
                    .build();

            for (Prediction response : client.predict(request).getPayloadList()) {
                System.out.printf("Predicted label: %s, Confidence: %.2f\n",
                        response.getDisplayName(), response.getClassification().getScore());
            }
        }
    }
}

}
