import threading
import time
import os
import random

# 1. Question Pool extracted from your images
# Format: "Question": [Option A, Option B, Option C, Option D, Correct Letter]
FULL_QUESTION_POOL = {
    "The velocity V of a transverse wave along a stretched string depends on the stress P, the density D and the length l. Find x, y, z in V = kP^x D^y l^z": 
        ["x=1, y=2, z=3", "x=1/2, y=-1/2, z=0", "x=1, y=2, z=1/2", "x=1, y=0, z=3", "B"],
    "Which of the following is the correct combination of dimensions for energy?": 
        ["MLT", "LT^2/M", "ML^2/T^2", "M^2L^3T", "C"],
    "Suppose A = B^n C^m where A has dimension LT, B has dimensions L^2T^-1 and C has dimension LT^2. Value of n?": 
        ["2/3", "2", "4/5", "1/5", "D"],
    "The pair of physical quantities that are scalar only are:": 
        ["Volume and area", "Moment and momentum", "Light and displacement", "None of the above", "A"],
    "The velocity of transverse waves in a string is v = kF^x μ^y. Values of x and y are:": 
        ["2 and 4", "-1/2 and 1/2", "1/2 and -1/2", "2 and 1/2", "C"],
    "Find the magnitude of the sum C = 4A + 3B where A = 10i + 3j + 7k and B = 6i - 9j + 4k": 
        ["58i - 39j + 40k", "58i - 39j + 16k", "22i - 15j + 40k", "58i - 15j + 40k", "D"],
    "Given D = 6i + 3j - k and E = 4i - 5j + 8k. Find the magnitude of difference 3D - E": 
        ["14i + 14j - 11k", "22i + 14j - 11k", "14i + 4j - 11k", "22i + 4j + 11k", "A"],
    "Two vectors of 10N and 20N are inclined at 60 degrees. Find the resultant:": 
        ["30.00N", "10.00N", "17.32N", "26.46N", "D"],
    "If force F = 2i + 3k and distance d = 4i - 2j + 2k, find workdone W = F.d": 
        ["12J", "14J", "10J", "17J", "B"],
    "If P = 3i + 4j - 6k and Q = 4i + 5k, find P x Q": 
        ["20i - 9j - 16k", "20i + 9j - 16k", "20i - 39j - 16k", "20i - 39j + 16k", "C"],
    "Find A x B if A = 2i + 4j and B = 5j + 3k": 
        ["12i + 6j - 10k", "12i - 6j + 10k", "12i - 6j - 10k", "12i + 6j + 10k", "D"],
    "A vector has components 10m (+x), 10m (+y), and 5m (+z). Magnitude is:": 
        ["zero", "15 m", "20 m", "25 m", "B"],
    "Find change in velocity of a car Vx = 30m/s + (2.5m/s^3)t^2 during t1=4s and t2=5.5s": 
        ["70.00 m/s", "105.63 m/s", "35.63 m/s", "175.63 m/s", "C"],
    "Ball thrown upward at 29.4 m/s. Time to reach highest point (g=9.8):": 
        ["44.1 m", "88.2 m", "22.1 m", "11.1 m", "A"], # Note: Question asks for time but options look like distance; usually 3s.
    "Particle projected at 12 m/s at 30 degrees. Time to reach max height (g=10):": 
        ["6 s", "12 s", "0.6 s", "1.2 s", "C"],
    "Find average velocity: t1=6.0s, x1=48.50m; t2=8.5s, x2=73.35m": 
        ["8.40 m/s", "9.94 m/s", "99.4 m/s", "84.0 m/s", "B"],
    "A car at 20 m/s stops in 10s with force of 5000N. Mass of the car is:": 
        ["1250 kg", "2500 kg", "5000 kg", "10000 kg", "B"],
    "Period of 6.4m pendulum on moon (g=1.6) is:": 
        ["1.57 s", "3.14 s", "12.56 s", "25.12 s", "C"],
    "Object thrown down at 1.00 m/s. After 5.00s (g=9.8), it travelled:": 
        ["125 m", "127.5 m", "245 m", "250 m", "B"],
    "Period is 4π seconds, amplitude 3.0m. Calculate max speed of particle:": 
        ["1 m/s", "2 m/s", "3 m/s", "1.5 m/s", "D"],
}

class PhysicsCBT:
    def __init__(self, num_questions=15, time_limit_mins=10):
        # Randomly select 15 questions from the pool
        keys = random.sample(list(FULL_QUESTION_POOL.keys()), min(num_questions, len(FULL_QUESTION_POOL)))
        self.test_questions = {k: FULL_QUESTION_POOL[k] for k in keys}
        
        self.time_limit = time_limit_mins * 60
        self.user_answers = {}
        self.time_up = False

    def timer(self):
        time.sleep(self.time_limit)
        if not self.time_up:
            self.time_up = True
            print("\n" + "="*40)
            print("TIME EXPIRED! Auto-submitting... Press Enter to view results.")
            print("="*40)

    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"--- PHYSICS CBT PRACTICE ---")
        print(f"Questions: {len(self.test_questions)} | Time: {self.time_limit//60} Minutes")
        print("-" * 30)
        input("Press Enter to begin...")

        threading.Thread(target=self.timer, daemon=True).start()

        for i, (q, details) in enumerate(self.test_questions.items(), 1):
            if self.time_up: break
            
            print(f"\n[{i}/{len(self.test_questions)}] {q}")
            print(f"A) {details[0]}")
            print(f"B) {details[1]}")
            print(f"C) {details[2]}")
            print(f"D) {details[3]}")
            
            ans = input("Your Choice (A/B/C/D): ").strip().upper()
            self.user_answers[q] = ans

        self.time_up = True
        self.show_results()

    def show_results(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- TEST RESULTS ---")
        score = 0
        for q, details in self.test_questions.items():
            correct = details[4]
            user = self.user_answers.get(q, "N/A")
            status = "CORRECT" if user == correct else f"WRONG (Correct: {correct})"
            if user == correct: score += 1
            print(f"Q: {q[:60]}...")
            print(f"You: {user} | Result: {status}\n")

        print(f"FINAL SCORE: {score}/{len(self.test_questions)}")
        print(f"Percentage: {(score/len(self.test_questions))*100:.1f}%")

if __name__ == "__main__":
    # Settings: 15 questions, 10 minutes
    test = PhysicsCBT(num_questions=15, time_limit_mins=10)
    test.run()
