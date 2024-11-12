var zendesk = new ZendeskApi("https://yoursubdomain.zendesk.com", "email", "api_token");
// Query the Answer Bot (illustrative example)
var answer = zendesk.AnswerBot.GetAnswer("How do I update my profile?");
Console.WriteLine(answer.Response);
