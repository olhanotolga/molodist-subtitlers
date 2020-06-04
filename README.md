# Molodist Subtitlers
## A knowledge base for Ukrainian film translators and subtitlers.

This is a repository.
The application is live at https://olhanotolga.pythonanywhere.com/.

### About the project

![homepage: screenshot](/subtitlers_app/static/images/subtitlers_homepage.png)

I’ve been meaning to put this project together since 2018. As an occasional translator for the [Molodist International Film Festival](https://molodist.com/en/) myself, I know how many questions arise once you start subtitling films! This is why I’ve tried to cover the basic information, examples, tools, and FAQs in this knowledge base.

The project is not finished. I plan on maintaining it and updating with new information.

I’m also planning to build a few tools to automate certain proofreading and editing tasks. For example, a program that would check if the manually added timecodes are in a proper order.

### The stack I used

Since I joined *FrauenLoop Web Development program*, I’ve been putting to practice the skills that I’ve acquired over January–April 2020: HTML, CSS, Bootstrap, Python, Flask, and, of course, Git and GitHub.

**The server part:** Python, Flask, Jinja.

**The client part:** HTML, Bootstrap for layout and styling, CSS for custom styling.

**Deployment:** [PythonAnywhere](https://www.pythonanywhere.com/).

### Project overview

![subtitling: screenshot](/subtitlers_app/static/images/subtitlers_subtitling.png)

#### Pages/Endpoints

The website consists of the following sections:
1. Home
2. About
3. Subtitling
4. Translating
5. Editing
6. Tools
7. FAQ

- It also has an Error page:

![error/404 page: screenshot](/subtitlers_app/static/images/subtitlers_error.png)

Each section corresponds to an endpoint (e.g. the About page is available at /about or the FAQ page is available at /faq etc.). Any other endpoint which is not associated with its own template returns the Error page.

#### Language

I decided to make it available in Ukrainian language only, as it’s the primary working language of my target audience.

For the demo purposes, some screenshots here are provided with the English content.

#### Responsiveness

The website is fully responsive, which has been achieved with Bootstrap, some CSS Flexbox, and media queries.
