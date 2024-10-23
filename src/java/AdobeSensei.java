import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

public class AdobeSenseiAPICall {
    public static void main(String[] args) {
        String accessToken = "YOUR_ACCESS_TOKEN";
        String apiUrl = "https://platform.adobe.io/data/sensei/mlServices";

        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpGet httpGet = new HttpGet(apiUrl);

        httpGet.setHeader("Authorization", "Bearer " + accessToken);
        httpGet.setHeader("x-gw-ims-org-id", "YOUR_ORGANIZATION_ID");
        httpGet.setHeader("x-api-key", "YOUR_API_KEY");

        try {
            HttpResponse response = httpClient.execute(httpGet);
            String responseBody = EntityUtils.toString(response.getEntity());
            System.out.println("API Response:");
            System.out.println(responseBody);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                httpClient.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
