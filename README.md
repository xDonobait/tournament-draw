# 🎲 Tournament Draw – Python

This Python script allows you to **organize a tournament draw with 16 duos**, dividing them into **4 pots based on their rating (1 to 5)** and randomly assigning them into **4 groups (A, B, C, D)**.  
It ensures that **no two duos from the same pot end up in the same group**.

---

## 🚀 Features
- ✅ Input of 16 duos with their ratings.  
- ✅ Automatic classification into 4 pots based on rating ranges.  
- ✅ Strict validation: **exactly 4 teams per pot**.  
- ✅ Random draw respecting the rule of 1 team per pot in each group.  
- ✅ Allows **repeating the draw** without re-entering the data.  
- ✅ Option to **save the result into `sorteo.txt`**.  

---

## 📌 Requirements
- Python **3.7 or higher**  
- No external libraries required (uses only Python standard modules)

---

## 🛠️ Installation
Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/yourusername/tournament-draw.git
cd tournament-draw
```

1. Enter the names and ratings for the 16 duos (you can input `3`, `3.5`, `4.25`, etc.).  
2. The program automatically classifies the duos into pots.  
3. The draw is performed and the groups are displayed in the console.  
4. You can save the result to `sorteo.txt` and repeat the draw as many times as needed.

---

## 📄 Example of the generated `sorteo.txt`

```
=== TOURNAMENT DRAW RESULT ===

Group A: Duo1, Duo5, Duo9, Duo13
Group B: Duo2, Duo6, Duo10, Duo14
Group C: Duo3, Duo7, Duo11, Duo15
Group D: Duo4, Duo8, Duo12, Duo16
```

## 📌 Default Rating Ranges
- **Pot 1:** 4.0 – 5.0  
- **Pot 2:** 3.0 – 3.99  
- **Pot 3:** 2.0 – 2.99  
- **Pot 4:** 1.0 – 1.99  

You can easily modify these in the `RANGOS` dictionary inside the code.
