# 🎬 Movie Rating Analysis Pipeline with MapReduce

This project implements a scalable, Hadoop-based MapReduce pipeline to process and analyze large-scale movie rating data. The pipeline identifies the top-rated movie(s) for each year, simulating distributed execution on both Hadoop and high-performance clusters like Condor.

---

## 🚀 Features

- **Mapper**: Parses and emits movie rating records as `(year, title)` pairs with their ratings.
- **Combiner**: Aggregates ratings and counts locally to reduce shuffle load.
- **Reducer**: Computes average ratings and selects top-rated movie(s) per year.
- **Cluster Ready**: Designed to scale to big data environments using Hadoop or HTCondor.

---

## 📂 Folder Structure


---

## 🛠️ How It Works

### ➤ Mapper
- Input: lines like `ID,Title,Genres,Year,Rating`
- Emits: `year,title \t rating\t1`
- Handles: multiple genres, filters years if `years.txt` is used.

### ➤ Combiner
- Aggregates `(year,title)` records by summing ratings and counts.
- Output: `year,title \t total_rating \t total_count`

### ➤ Reducer
- Computes average ratings per `(year, title)`
- Outputs top movie(s) for each year: `year, title, avg_rating`

---

## 🧪 Run Instructions

### 🖥 Simulate Locally
```bash
bash run/simhadoop.sh


🧵 Run on Hadoop
bash run/runhadoop.sh
