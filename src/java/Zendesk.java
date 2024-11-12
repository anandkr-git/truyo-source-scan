Zendesk zendesk = new Zendesk.Builder("https://yoursubdomain.zendesk.com").build();
// Hypothetical AnswerBot or AI request
AnswerResponse answer = zendesk.answerBot().getAnswer("How do I reset my password?");
System.out.println(answer.getAnswerText());
