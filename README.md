# UCB-AI-Hack---BlurtAI
An AI application that takes in notes from the user and provides them with a comprehensive learning experience

Name: Blurt.AI

Purpose: The inspiration behind the project is the Feynman Technique; this technique involves the learner to test/explain what they already know to see where the holes in the learning exist. Then the learner is supposed to fill in these holes to get a comprehensive understanding of the subject. Our program intends to serve as a modern learning tool using the Feynman Technique.

The logistics fo the project: The user (student) enters a pdf of class notes into the program. Then, the program creates a pre-test based on the notes to see how much information they already know/ have mastered.  There should be a status bar at the top of the program to indicate the percentage of the subject the user knows. After the pre-test, the user should get a report on where their holes in knowledge exist. Then, the program provides flashcards for studying process. Finally, a test is given to examine how much information the user knows after studying.

Technologies and Frameworks that will be used:
- Python
- Next.js (for the frontend)
- Flask (to connect the python backend with the frontend)
- OpenAI API (LLM to read in the notes from user and curate the information)
