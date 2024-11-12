$projectId = "your_project_id";
$modelId = "your_model_id";
$imagePath = "path_to_your_image.jpg";
$accessToken = "your_oauth_access_token";  // Obtain this through OAuth

$url = "https://automl.googleapis.com/v1/projects/$projectId/locations/us-central1/models/$modelId:predict";

$imageData = file_get_contents($imagePath);
$payload = [
    "payload" => [
        "image" => [
            "imageBytes" => base64_encode($imageData)
        ]
    ]
];

$options = [
    "http" => [
        "header"  => "Authorization: Bearer " . $accessToken . "\r\n" .
                     "Content-Type: application/json\r\n",
        "method"  => "POST",
        "content" => json_encode($payload),
    ],
];

$context  = stream_context_create($options);
$response = file_get_contents($url, false, $context);

echo $response;
