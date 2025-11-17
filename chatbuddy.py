import tkinter as tk 
from tkinter import scrolledtext


# ----------------- Formula Function -----------------
def maths_formulas(user_input):
    user_input = user_input.lower()
    words = user_input.split()

    # ---------------- GEOMETRY (CLASS 6–10) ----------------
    if 'rectangle' in words and 'perimeter' in words:
        return "Perimeter of Rectangle = 2 * (length + breadth)"
    elif 'rectangle' in words and 'area' in words:
        return "Area of Rectangle = length * breadth"
    elif 'square' in words and 'perimeter' in words:
        return "Perimeter of Square = 4 * side"
    elif 'square' in words and 'area' in words:
        return "Area of Square = side²"
    elif 'circle' in words and 'area' in words:
        return "Area of Circle = π * radius²"
    elif 'circle' in words and ('circumference' in words or 'perimeter' in words):
        return "Circumference of Circle = 2 * π * radius"
    elif 'triangle' in words and 'area' in words:
        return "Area of Triangle = 0.5 * base * height"
    elif 'parallelogram' in words and 'area' in words:
        return "Area = base * height"
    elif 'trapezium' in words and 'area' in words:
        return "Area = 0.5 * (sum of parallel sides) * height"
    elif 'rhombus' in words and 'area' in words:
        return "Area = 0.5 * d1 * d2"
    elif 'cube' in words and 'volume' in words:
        return "Volume = side³"
    elif 'cuboid' in words and 'volume' in words:
        return "Volume = length * breadth * height"
    elif 'sphere' in words and 'volume' in words:
        return "Volume = (4/3) * π * radius³"
    elif 'cone' in words and 'volume' in words:
        return "Volume = (1/3) * π * radius² * height"
    elif 'cylinder' in words and 'volume' in words:
        return "Volume = π * radius² * height"

    # ------------ ADDITIONAL GEOMETRY (CLASS 11–12) ------------
    elif 'equilateral' in words and 'triangle' in words and 'area' in words:
        return "Area = (√3 / 4) * side²"
    elif 'heron' in words:
        return "Heron's Formula: Area = √(s(s-a)(s-b)(s-c)); s = (a+b+c)/2"
    elif 'hemisphere' in words and 'volume' in words:
        return "Volume = (2/3) * π * r³"
    elif 'hemisphere' in words and 'surface' in words:
        return "TSA = 3πr², CSA = 2πr²"

    # ---------------- TRIGONOMETRY BASIC ----------------
    elif 'tan' in words:
        return "tanθ = sinθ / cosθ"
    elif 'sec' in words:
        return "secθ = 1 / cosθ"
    elif 'cosec' in words:
        return "cosecθ = 1 / sinθ"
    elif 'cot' in words:
        return "cotθ = cosθ / sinθ"
    elif 'sin^2' in user_input and 'cos^2' in user_input:
        return "sin²θ + cos²θ = 1"

    # ---------------- TRIGONOMETRY ADVANCED (11–12) ----------------
    elif 'sin(a+b)' in user_input or 'cos(a+b)' in user_input or 'trigonometric' in words:
        return "sin(A±B)=sinAcosB±cosAsinB,  cos(A±B)=cosAcosB∓sinAsinB"
    elif 'double' in words or '2a' in user_input:
        return "sin2A=2sinAcosA,  cos2A=1−2sin²A=2cos²A−1"
    elif 'half' in words and 'angle' in words:
        return "sin(A/2)=√((1−cosA)/2), cos(A/2)=√((1+cosA)/2)"

    # ---------------- ALGEBRA (11–12) ----------------
    elif '(a+b)^2' in user_input:
        return "(a+b)² = a² + 2ab + b²"
    elif '(a-b)^2' in user_input:
        return "(a−b)² = a² − 2ab + b²"
    elif 'a^2 - b^2' in user_input:
        return "a² − b² = (a+b)(a−b)"
    elif '(a+b)^3' in user_input:
        return "(a+b)³ = a³ + b³ + 3ab(a+b)"
    elif '(a-b)^3' in user_input:
        return "(a−b)³ = a³ − b³ − 3ab(a−b)"

    # ---------------- SEQUENCES & SERIES ----------------
    elif 'ap' in words and 'nth' in words:
        return "Nth term of AP = a + (n-1)d"
    elif 'ap' in words and 'sum' in words:
        return "Sum of AP = (n/2)*(2a + (n-1)d)"
    elif 'gp' in words and 'nth' in words:
        return "Nth term of GP = ar^(n-1)"
    elif 'gp' in words and 'sum' in words:
        return "Sum of GP (finite) = a*(r^n - 1)/(r - 1)"

    # ---------------- CALCULUS: LIMITS ----------------
    elif 'limit' in words and 'sinx/x' in user_input:
        return "lim (sinx/x) as x→0 = 1"
    elif 'limit' in words and '1-cos' in user_input:
        return "lim (1 - cosx)/x² as x→0 = 1/2"

    # ---------------- CALCULUS: DERIVATIVES ----------------
    elif 'derivative' in words and 'x^n' in user_input:
        return "d(x^n)/dx = n*x^(n-1)"
    elif 'derivative' in words and 'sin' in words:
        return "d(sin x)/dx = cos x"
    elif 'derivative' in words and 'cos' in words:
        return "d(cos x)/dx = -sin x"
    elif 'derivative' in words and 'tan' in words:
        return "d(tan x)/dx = sec² x"
    elif 'product' in words and 'rule' in words:
        return "(uv)' = u'v + uv'"
    elif 'quotient' in words and 'rule' in words:
        return "(u/v)' = (u'v - uv')/v²"
    elif 'chain' in words and 'rule' in words:
        return "dy/dx = (dy/du)*(du/dx)"

    # ---------------- CALCULUS: INTEGRATION ----------------
    elif 'integrate' in words and 'x^n' in user_input:
        return "∫x^n dx = x^(n+1)/(n+1) + C"
    elif 'integrate' in words and '1/x' in user_input:
        return "∫1/x dx = ln|x| + C"
    elif 'integrate' in words and 'sin' in words:
        return "∫sin x dx = -cos x + C"
    elif 'integrate' in words and 'cos' in words:
        return "∫cos x dx = sin x + C"
    elif 'integrate' in words and 'sec^2' in user_input:
        return "∫sec²x dx = tan x + C"

    # ---------------- COMPLEX NUMBERS (11–12) ----------------
    elif 'modulus' in words:
        return "|z| = √(x² + y²)"
    elif 'argument' in words:
        return "arg(z) = tan⁻¹(y/x)"
    elif 'conjugate' in words:
        return "z̄ = x - iy"
    elif 'euler' in words:
        return "Euler’s Formula: e^(iθ) = cosθ + i sinθ"

    # ---------------- PERMUTATION & COMBINATION ----------------
    elif 'npr' in user_input:
        return "nPr = n! / (n-r)!"
    elif 'ncr' in user_input:
        return "nCr = n! / (r!(n-r)!)"

    # ---------------- BINOMIAL THEOREM ----------------
    elif 'binomial' in words:
        return "(a+b)^n = Σ[nCk * a^(n-k) * b^k]"

    # ---------------- COORDINATE GEOMETRY ----------------
    elif 'distance' in words:
        return "Distance = √((x2-x1)² + (y2-y1)²)"
    elif 'midpoint' in words:
        return "Midpoint = ((x1+x2)/2, (y1+y2)/2)"
    elif 'section' in words:
        return "((mx2+nx1)/(m+n), (my2+ny1)/(m+n))"
    elif 'centroid' in words:
        return "Centroid = ((x1+x2+x3)/3 , (y1+y2+y3)/3)"
    elif 'triangle' in words and 'coordinate' in words:
        return "Area = 0.5|x1(y2-y3)+x2(y3-y1)+x3(y1-y2)|"

    # ---------------- VECTORS & 3D GEOMETRY ----------------
    elif 'vector' in words and 'magnitude' in words:
        return "|a| = √(a1² + a2² + a3²)"
    elif 'dot' in words:
        return "a·b = a1b1 + a2b2 + a3b3"
    elif 'cross' in words:
        return "|a×b| = |a||b| sinθ"
    elif 'plane' in words:
        return "ax + by + cz + d = 0"

    # ---------------- GREETINGS ----------------
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "name" in user_input:
        return "I am ChatBuddy, your Virtual Maths Assistant."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"

    # ---------------- DEFAULT ----------------
    else:
        return "I’m not fully sure, but I am learning every day!"


# ------------------ SEND MESSAGE FUNCTION ------------------
def send_message():
    user_input = entry_field.get().strip()
    if not user_input:
        return

    entry_field.delete(0, tk.END)

    bot_reply = maths_formulas(user_input)

    chat_area.config(state='normal')

    chat_area.insert(tk.END, f"\nYou:\n", "user_tag")
    chat_area.insert(tk.END, f"{user_input}\n")

    chat_area.insert(tk.END, f"\nChatBuddy:\n", "bot_tag")
    chat_area.insert(tk.END, f"{bot_reply}\n")

    chat_area.config(state='disabled')
    chat_area.yview(tk.END)


# ------------------ MAIN WINDOW ------------------
root = tk.Tk()
root.title("ChatBuddy - Maths Assistant")
root.geometry("420x590")
root.resizable(False, False)
root.configure(bg="#7232FC")


# ------------------ CHAT AREA ------------------
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    state='disabled',
    font=("Calibri", 15, "bold"),
    bg="#7232FC",
    fg="#FFED63",
    bd=0
)
chat_area.place(x=10, y=10, width=400, height=480)


# ------------------ TAG STYLES ------------------
chat_area.tag_config(
    "user_tag",
    foreground="#FFED63",
    background="#7232FC",
    font=("Calibri", 12, "bold"),
    justify="left",
    rmargin=5
)

chat_area.tag_config(
    "bot_tag",
    foreground="#FFED63",
    background="#7232FC",
    font=("Calibri", 15, "bold"),
    justify="left",
    lmargin1=5
)


# ------------------ AUTOMATIC GREETING ------------------
chat_area.config(state='normal')
chat_area.insert(tk.END, "ChatBuddy:\n")
chat_area.insert(tk.END, "Hello! I am your Virtual Friend \n")
chat_area.config(state='disabled')
chat_area.yview(tk.END)


# ------------------ ENTRY FIELD ------------------
entry_field = tk.Entry(
    root,
    font=("Calibri", 14, "bold"),
    bg="#FFED63",
    fg="#7232FC",
    bd=2,
    relief="flat"
)
entry_field.place(x=10, y=505, width=300, height=40)
entry_field.bind("<Return>", lambda event: send_message())

entry_field.focus()


# ------------------ SEND BUTTON ------------------
send_btn = tk.Button(
    root,
    text="Ask",
    font=("Calibri", 16, "bold"),
    bg="#FFED63",
    fg="#7232FC",
    activebackground="#FFED63",
    activeforeground="#7232FC",
    bd=0,
    command=send_message
)
send_btn.place(x=320, y=505, width=90, height=40)


root.mainloop()
