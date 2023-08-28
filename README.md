<h1 align="center">
 <br>
 MovieCritic.AI
</h1>

MovieCritic is an LLM powered bot built to specialize in movie recommendations based on interactions with users. The more users interact with the bot, the better the bot's movie recommendations. For now, the backend of MovieCritic is connected to a sandbox Movie database on Neo4j.

### Quickstart

1. Ensure requirements are installed (virtual environment recommended).
2. Run `python moviecritic/main.py` in your terminal.
3. Enter `OpenAI`, `Neo4j` credentials
4. Chat with MovieCritic.AI
5. See movie recommendations!

### Sample Output

```
MovieCritic.AI: Great. Let's get started. How can I help?
        
Me: How many movies are you aware of?

MovieCritic.AI: I am aware of 38 movies.

Me: That's cool.

MovieCritic.AI: Yes, it is cool!

Me: Are you familiar with any movies from the 80s?          

MovieCritic.AI: Yes, I am familiar with movies from the 80s. Some popular movies from that decade include "Top Gun" and "Stand By Me."

Me: I love Stand By Me!

MovieCritic.AI: I'm glad to hear that you love Stand By Me! It's a fantastic movie that features a talented cast including Jerry O'Connell, River Phoenix, Marshall Bell, Wil Wheaton, Kiefer Sutherland, John Cusack, and Corey Feldman. Their performances really bring the story to life.

Me: If I enjoy the movie Stand By Me, what other movies might I enjoy?

MovieCritic.AI: If you enjoy the movie Stand By Me, you might also enjoy other coming-of-age films such as The Goonies, The Sandlot, or Dead Poets Society. These movies share similar themes of friendship, adventure, and self-discovery that make Stand By Me so enjoyable.
```