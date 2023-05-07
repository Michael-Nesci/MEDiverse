import cohere
from cohere.responses.classify import Example

review = input("Please enter your review: ")

co = cohere.Client('11QsMFSeh7hidclWcFvlIb5tQ7y3xtfaXJK30AOW')  # This is your trial API key

pos_or_neg = co.classify(
    model='large',
    inputs=[review],
    examples=[
        Example("Dr Green was very kind and helpful when I asked about gender affirming care options.", "Positive"),
        Example(
            "I did not like my experience at the Health Clinic. The staff were homophobic and I felt judged during my visit.",
            "Negative"), Example("Great place to get birth control, no questions asked!", "Positive"), Example(
            "I asked if I could get gender replacement surgery and was asked why I would even want to do that to myself. Do not recommend.",
            "Negative"),
        Example("I came here to chat about sexual health and safety and my doctor was respectful and knowledgeable.",
                "Positive"), Example(
            "I brought up my concerns regarding my hormone levels and Doctor Brown told me that if I was thinking about HRT to forget it because she would not prescribe it to me and didn\'t believe in gender dysphoria.",
            "Negative"), Example(
            "\"I was very pleased with the care I received from Dr. Smith. I was looking for a LGBTQ+ friendly doctor, and I found him to be very understanding and supportive. I would definitely recommend him to others.\"",
            "Positive"), Example(
            "\"I was referred to Dr. Smith by my primary care physician, and I am so glad I decided to take their advice. I was looking for a doctor who would be LGBTQ+ friendly and understanding of my needs, and he has exceeded all of my expectations. He is very compassionate and has always made sure to address all of my concerns.\"",
            "Positive"), Example(
            "\"The doctor was very compassionate and understanding of my situation. I felt like I could be honest and open about my health concerns.\"",
            "Positive"), Example(
            "\"The doctor was very understanding and supportive of my decision to transition. I felt comfortable and respected during my appointment.\"",
            "Positive"), Example(
            "\"I was very disappointed with the lack of understanding and empathy from Dr. X. I visited his office seeking advice and treatment for my LGBTQ+ identity, and he was very dismissive and rude. He refused to acknowledge my feelings or provide any sort of support, and instead just tried to give me a bunch of medication. I felt very invalidated and alone, and I would not recommend him to anyone.\"",
            "Negative"), Example(
            "\"I was very upset with the way this doctor handled my gender-affirming treatment. I felt like I was being pushed to make a decision about my transition without really being given the time or space to process my feelings or think about what might work best for me.\"",
            "Negative"), Example(
            "\"I went to this doctor for a referral to a sexuality counselor. He refused to give me one and instead tried to convince me that I was confused about my sexuality. I ended up leaving in tears and never going back.\"",
            "Negative"), Example(
            "\"I have been seeing this doctor for many years. They have always been very LGBTQ+ friendly and understanding. I feel very comfortable discussing my medical concerns with them, and they have always been very helpful in providing me with the best care. I highly recommend this doctor to any LGBTQ+ patient.\"",
            "Positive"), Example(
            "\"I was looking for a doctor who was LGBTQ+ friendly and willing to help me with my specific medical needs. I am so glad I found Dr. D, as they were able to provide me with the care I needed and made me feel comfortable and accepted. I would highly recommend Dr. D to anyone looking for a LGBTQ+ friendly doctor.\"",
            "Positive"), Example(
            "\"I recently visited Dr. Smith for a routine check-up. As a queer patient, I was nervous about finding a doctor who would be sensitive to my needs. However, Dr. Smith was incredibly kind and understanding. He asked me a variety of questions about my medical history and made me feel comfortable throughout the entire appointment. I would highly recommend Dr. Smith to any queer patient looking for a doctor who will treat them with compassion and respect.\"",
            "Positive"), Example(
            "\"I would not recommend this doctor to anyone, let alone a queer patient. I visited this doctor for LGBTQ+ medical advice and they were completely useless.\"",
            "Negative"), Example(
            "\"I am appalled by the way this doctor treated me. I visited them for LGBTQ+ medical advice and they were very patronizing and condescending.\"",
            "Negative"), Example(
            "\"This doctor is not queer-friendly. I felt very uncomfortable and like I couldn\'t be honest about my condition.\"",
            "Negative"), Example(
            "\"I went to this doctor for a sinus infection and was horrified when he made a number of comments about my sexual orientation. I found this extremely offensive and I left his office feeling discriminated against.\"",
            "Negative")])

eiuol = ('The confidence levels of the labels are: {}'.format(pos_or_neg.classifications)).split(",")
prediction = eiuol[0].split(": ")[-1]
prediction = prediction[1:-1].lower()
if prediction == "positive":
    print(f"This was a \033[1;32m{prediction.upper()}\033[0m experience")
else:
    print(f"This was a \033[1;31m{prediction.upper()}\033[0m experience")

flair = co.classify(
    model='large',
    inputs=[review],
    examples=[Example("Dr Green was very kind and helpful when I asked about gender affirming care options.",
                      "Trans Friendly"), Example(
        "I did not like my experience at the Health Clinic. The staff were homophobic and I felt judged during my visit.",
        "Homophobic"), Example("Great place to get birth control, no questions asked!", "Trans Friendly"),
              Example(
                  "I asked if I could get gender replacement surgery and was asked why I would even want to do that to myself. Do not recommend.",
                  "Homophobic"), Example(
            "I came here to chat about sexual health and safety and my doctor was respectful and knowledgeable.",
            "Informed Consent"), Example(
            "I brought up my concerns regarding my hormone levels and Doctor Brown told me that if I was thinking about HRT to forget it because she would not prescribe it to me and didn\\'t believe in gender dysphoria.",
            "Homophobic"), Example(
            "I was very pleased with the care I received from Dr. Smith. I was looking for a LGBTQ+ friendly doctor, and I found him to be very understanding and supportive. I would definitely recommend him to others.",
            "Trans Friendly"), Example(
            "I was very pleased with the care I received from Dr. Smith. I was looking for a LGBTQ+ friendly doctor, and I found him to be very understanding and supportive. I would definitely recommend him to others.",
            "Informed Consent"), Example(
            "I was referred to Dr. Smith by my primary care physician, and I am so glad I decided to take their advice. I was looking for a doctor who would be LGBTQ+ friendly and understanding of my needs, and he has exceeded all of my expectations. He is very compassionate and has always made sure to address all of my concerns.",
            "Trans Friendly"), Example(
            "The doctor was very compassionate and understanding of my situation. I felt like I could be honest and open about my health concerns.",
            "Trans Friendly"), Example(
            "The doctor was very understanding and supportive of my decision to transition. I felt comfortable and respected during my appointment.",
            "Trans Friendly"), Example(" not racially friendly", "Racist"),
              Example("racially friendly", "Racial quity"), Example(
            "I was very disappointed with the lack of understanding and empathy from Dr. X. I visited his office seeking advice and treatment for my LGBTQ+ identity, and he was very dismissive and rude. He refused to acknowledge my feelings or provide any sort of support, and instead just tried to give me a bunch of medication. I felt very invalidated and alone, and I would not recommend him to anyone.\n\n",
            "Homophobic"), Example(
            "I was very upset with the way this doctor handled my gender-affirming treatment. I felt like I was being pushed to make a decision about my transition without really being given the time or space to process my feelings or think about what might work best for me.",
            "Homophobic"), Example(
            "I went to this doctor for a referral to a sexuality counselor. He refused to give me one and instead tried to convince me that I was confused about my sexuality. I ended up leaving in tears and never going back.",
            "Homophobic"), Example(
            "I have been seeing this doctor for many years. They have always been very LGBTQ+ friendly and understanding. I feel very comfortable discussing my medical concerns with them, and they have always been very helpful in providing me with the best care. I highly recommend this doctor to any LGBTQ+ patient.",
            "Trans Friendly"), Example(
            "I recently visited Dr. Smith for a routine check-up. As a queer patient, I was nervous about finding a doctor who would be sensitive to my needs. However, Dr. Smith was incredibly kind and understanding. He asked me a variety of questions about my medical history and made me feel comfortable throughout the entire appointment. I would highly recommend Dr. Smith to any queer patient looking for a doctor who will treat them with compassion and respect.",
            "Trans Friendly"), Example(
            "I would not recommend this doctor to anyone, let alone a queer patient. I visited this doctor for LGBTQ+ medical advice and they were completely useless.",
            "Homophobic"), Example(
            "I am appalled by the way this doctor treated me. I visited them for LGBTQ+ medical advice and they were very patronizing and condescending.",
            "Homophobic"), Example(
            "This doctor is not queer-friendly. I felt very uncomfortable and like I couldn\\'t be honest about my condition.",
            "Homophobic"), Example(
            "I went to this doctor for a sinus infection and was horrified when he made a number of comments about my sexual orientation. I found this extremely offensive and I left his office feeling discriminated against.",
            "Homophobic"), Example(
            "I\'m so glad I found this practice! The staff is very friendly and helpful. I feel comfortable and respected as a patient.",
            "Trans Friendly"), Example(
            "The staff was very friendly and understanding. They made sure I was comfortable and respected my privacy. I would definitely recommend this office to other LGBTQ patients.",
            "Trans Friendly"), Example(
            "I am a gay man and I have always felt welcome and accepted at this office. They have gone above and beyond to make sure I have the resources and support I need, and they have been very responsive to my needs. I am very grateful for their services.",
            "Trans Friendly"), Example(
            "I am a lesbian and I have always felt comfortable and accepted at this office. The staff is very friendly and helpful, and they have always treated me with respect and understanding. I highly recommend them.",
            "Trans Friendly"), Example(
            "I am a bisexual woman and I have always felt welcomed and accepted at this office. They have gone above and beyond to make sure I have the resources and support I need, and they have been very responsive to my needs. I am very grateful for their services",
            "Trans Friendly"), Example(
            "I am a transgender man and I have always felt welcomed and accepted at this office. The staff is very friendly and helpful, and they have always treated me with respect and understanding. I highly recommend them.",
            "Trans Friendly"), Example("racially inclusive", "Racial quity"),
              Example("not racially inclusive", "Racist")])

raw_print_statement_flair = ('The confidence levels of the labels are: {}'.format(flair.classifications)).split(",")
prediction_flair = raw_print_statement_flair[0].split(": ")[-1]
prediction_flair = prediction_flair[1:-1].lower()
print(f"Flair: \033[01m{prediction_flair.title()}\033[0m")
