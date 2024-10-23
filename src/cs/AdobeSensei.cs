using System.Net.Http;
using System.Net.Http.Headers;

public class AdobeSenseiAPICall {
    public static async Task Main() {
        string accessToken = "YOUR_ACCESS_TOKEN";
        string apiUrl = "https://platform.adobe.io/data/sensei/mlServices";

        using (HttpClient httpClient = new HttpClient())
        {
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", accessToken);
            httpClient.DefaultRequestHeaders.Add("x-gw-ims-org-id", "YOUR_ORGANIZATION_ID");
            httpClient.DefaultRequestHeaders.Add("x-api-key", "YOUR_API_KEY");

            HttpResponseMessage response = await httpClient.GetAsync(apiUrl);
            response.EnsureSuccessStatusCode();

            string responseBody = await response.Content.ReadAsStringAsync();
            Console.WriteLine("API Response:");
            Console.WriteLine(responseBody);
        }
    }
}
