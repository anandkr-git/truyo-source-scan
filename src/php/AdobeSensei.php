<?php
$accessToken = "YOUR_ACCESS_TOKEN";
$apiUrl = "https://platform.adobe.io/data/sensei/mlServices";

$client = new GuzzleHttp\Client();
$headers = [
    'Authorization' => 'Bearer ' . $accessToken,
    'x-gw-ims-org-id' => 'YOUR_ORGANIZATION_ID',
    'x-api-key' => 'YOUR_API_KEY'
];

try {
    $response = $client->get($apiUrl, ['headers' => $headers]);
    $responseBody = $response->getBody()->getContents();
    echo "API Response:\n";
    echo $responseBody;
} catch (\GuzzleHttp\Exception\GuzzleException $e) {
    echo 'Error: ' . $e->getMessage();
}
