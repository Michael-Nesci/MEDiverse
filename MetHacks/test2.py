import cohere
from cohere.responses.classify import Example
import json


co = cohere.Client('11QsMFSeh7hidclWcFvlIb5tQ7y3xtfaXJK30AOW') # This is your trial API key
# user_input = input("Enter your review: ")


raw_data = open("rawdata.txt", "r")
raw_data = raw_data.readlines()



    #look through the raw data and write the prediction to the file in a dictionary key as the review value as a list in the format[predication_, prediction_flair]
target = open("Smith.txt", "a")

for line in raw_data:
  line = line.split(",")
  if line[-2] == "Smith":
      response = co.classify(
        model='large',
        inputs=[str(line[0:-2])],
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
      eiuol = ('The confidence levels of the labels are: {}'.format(response.classifications)).split(",")
      prediction = eiuol[0].split(": ")[-1]
      prediction = prediction[1:-1].lower()
      print(f"This was a {prediction.upper()} experience")

      flair = co.classify(
        model='large',
        inputs=[str(line[0:-2])],
        examples=[
          Example("Dr Green was very kind and helpful when I asked about gender affirming care options.",
                  "LGBTQ friendly"),
          Example(
            "I did not like my experience at the Health Clinic. The staff were homophobic and I felt judged during my visit.",
            "homophobic"), Example("Great place to get birth control, no questions asked!", "LGBTQ friendly"), Example(
            "I asked if I could get gender replacement surgery and was asked why I would even want to do that to myself. Do not recommend.",
            "homophobic"),
          Example("I came here to chat about sexual health and safety and my doctor was respectful and knowledgeable.",
                  "informed consent"), Example(
            "I brought up my concerns regarding my hormone levels and Doctor Brown told me that if I was thinking about HRT to forget it because she would not prescribe it to me and didn\\'t believe in gender dysphoria.",
            "homophobic"), Example(
            "I was very pleased with the care I received from Dr. Smith. I was looking for a LGBTQ+ friendly doctor, and I found him to be very understanding and supportive. I would definitely recommend him to others.",
            "LGBTQ friendly"), Example(
            "I was very pleased with the care I received from Dr. Smith. I was looking for a LGBTQ+ friendly doctor, and I found him to be very understanding and supportive. I would definitely recommend him to others.",
            "informed consent"), Example(
            "I was referred to Dr. Smith by my primary care physician, and I am so glad I decided to take their advice. I was looking for a doctor who would be LGBTQ+ friendly and understanding of my needs, and he has exceeded all of my expectations. He is very compassionate and has always made sure to address all of my concerns.",
            "LGBTQ friendly"), Example(
            "The doctor was very compassionate and understanding of my situation. I felt like I could be honest and open about my health concerns.",
            "LGBTQ friendly"), Example(
            "The doctor was very understanding and supportive of my decision to transition. I felt comfortable and respected during my appointment.",
            "LGBTQ friendly"), Example("was racist", "racist"), Example("was not racist", "racial equity"),
          Example("was not racially understanding", "racist"), Example("was racially understanding", "racial equity"),
          Example(
            "I was very disappointed with the lack of understanding and empathy from Dr. X. I visited his office seeking advice and treatment for my LGBTQ+ identity, and he was very dismissive and rude. He refused to acknowledge my feelings or provide any sort of support, and instead just tried to give me a bunch of medication. I felt very invalidated and alone, and I would not recommend him to anyone.\n\n",
            "homophobic"), Example(
            "I was very upset with the way this doctor handled my gender-affirming treatment. I felt like I was being pushed to make a decision about my transition without really being given the time or space to process my feelings or think about what might work best for me.",
            "homophobic"), Example(
            "I went to this doctor for a referral to a sexuality counselor. He refused to give me one and instead tried to convince me that I was confused about my sexuality. I ended up leaving in tears and never going back.",
            "homophobic"), Example(
            "I have been seeing this doctor for many years. They have always been very LGBTQ+ friendly and understanding. I feel very comfortable discussing my medical concerns with them, and they have always been very helpful in providing me with the best care. I highly recommend this doctor to any LGBTQ+ patient.",
            "LGBTQ friendly")])

      raw_print_statement_flair = ('The confidence levels of the labels are: {}'.format(flair.classifications)).split(",")
      prediction_flair = raw_print_statement_flair[0].split(": ")[-1]
      prediction_flair = prediction_flair[1:-1].lower()


      target.write(f"{line[0:-2]}:[{prediction}, {prediction_flair}]\n,")




