
endpoint_config_name = 'tabular_explainer_endpoint_config'
response = sagemaker_client.create_endpoint_config(
    EndpointConfigName=endpoint_config_name,
    ProductionVariants=[{
        'VariantName': 'AllTraffic',
        'ModelName': model_name,
        'InitialInstanceCount': 1,
        'InstanceType': 'ml.m5.xlarge',
    }],
    ExplainerConfig={
        'ClarifyExplainerConfig': {
            'ShapConfig': {
                'ShapBaselineConfig': {
                    'ShapBaseline': '0,0,0,0',
                },
            },
        },
    },
)
            