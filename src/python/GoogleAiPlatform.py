from googleaiplatform.cloud import 
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value


def create_batch_prediction_job_sample(
    project: str,
    display_name: str,
    model_name: str,
    instances_format: str,
    gcs_source_uri: str,
    predictions_format: str,
    gcs_destination_output_uri_prefix: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.JobServiceClient(client_options=client_options)
    model_parameters_dict = {}
    model_parameters = json_format.ParseDict(model_parameters_dict, Value())

    batch_prediction_job = {
        "display_name": display_name,
        # Format: 'projects/{project}/locations/{location}/models/{model_id}'
        "model": model_name,
        "model_parameters": model_parameters,
        "input_config": {
            "instances_format": instances_format,
            "gcs_source": {"uris": [gcs_source_uri]},
        },
        "output_config": {
            "predictions_format": predictions_format,
            "gcs_destination": {"output_uri_prefix": gcs_destination_output_uri_prefix},
        },
        "dedicated_resources": {
            "machine_spec": {
                "machine_type": "n1-standard-2",
                "accelerator_type": aiplatform.gapic.AcceleratorType.NVIDIA_TESLA_K80,
                "accelerator_count": 1,
            },
            "starting_replica_count": 1,
            "max_replica_count": 1,
        },
    }
    parent = f"projects/{project}/locations/{location}"
    response = client.create_batch_prediction_job(
        parent=parent, batch_prediction_job=batch_prediction_job
    )
    print("response:", response)

