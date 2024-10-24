use Google\ApiCore\ApiException;
use Google\ApiCore\OperationResponse;
use Google\Cloud\AIPlatform\V1\Client\DatasetServiceClient;
use Google\Cloud\AIPlatform\V1\CreateDatasetVersionRequest;
use Google\Cloud\AIPlatform\V1\DatasetVersion;
use Google\Protobuf\Value;
use Google\Rpc\Status;

/**
 * @param string $formattedParent The name of the Dataset resource.
 *                                Format:
 *                                `projects/{project}/locations/{location}/datasets/{dataset}`
 *                                Please see {@see DatasetServiceClient::datasetName()} for help formatting this field.
 */
function create_dataset_version_sample(string $formattedParent): void
{
    // Create a client.
    $datasetServiceClient = new DatasetServiceClient();

    // Prepare the request message.
    $datasetVersionMetadata = new Value();
    $datasetVersion = (new DatasetVersion())
        ->setMetadata($datasetVersionMetadata);
    $request = (new CreateDatasetVersionRequest())
        ->setParent($formattedParent)
        ->setDatasetVersion($datasetVersion);

    // Call the API and handle any network failures.
    try {
        /** @var OperationResponse $response */
        $response = $datasetServiceClient->createDatasetVersion($request);
        $response->pollUntilComplete();

        if ($response->operationSucceeded()) {
            /** @var DatasetVersion $result */
            $result = $response->getResult();
            printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
        } else {
            /** @var Status $error */
            $error = $response->getError();
            printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
        }
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }
}

/**
 * Helper to execute the sample.
 *
 * This sample has been automatically generated and should be regarded as a code
 * template only. It will require modifications to work:
 *  - It may require correct/in-range values for request initialization.
 *  - It may require specifying regional endpoints when creating the service client,
 *    please see the apiEndpoint client configuration option for more details.
 */
function callSample(): void
{
    $formattedParent = DatasetServiceClient::datasetName('[PROJECT]', '[LOCATION]', '[DATASET]');

    create_dataset_version_sample($formattedParent);
}
