### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "5d4c88f9d7767dbc357fdaa8c32ed1b368064bf844a2bd8caab1ac6af0729734"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3
    else: 

        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    questions = [
    "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?",
    "Are encoding and encryption the same? - Yes/No",
    "Is it possible to decrypt a message without a key? - Yes/No",
    "Is it possible to decode a message without a key? - Yes/No",
    "Is a hashed message supposed to be un-hashed? - Yes/No",
    "What is the SHA256 hashing value of your NYU email and use the answer in your code - ",
    "Is MD5 a secured hashing algorithm? - Yes/No",
    "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number",
    "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number",
    "What is a jeporady?"
]
    for question in questions:
        print(f"Question: {question}")
        print(f"Answer: {welcome_assignment_answers(question)}\n")

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
