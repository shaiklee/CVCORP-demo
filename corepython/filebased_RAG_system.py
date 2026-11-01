# PROJECT 2: FILE-BASED RAG SYSTEM
def build_index(file):

    with open(file, "r") as f, open("vector_store.txt", "w") as vs:
        chunk = []
        for line in f:
            chunk.append(line.strip())

            if len(chunk) == 2:
                combined = " ".join(chunk)
                vs.write(combined + "\n")
                chunk = []

        if chunk:
            vs.write(" ".join(chunk) + "\n")
def query_system():

    while True:
        query = input("\nAsk (type 'exit'): ")

        if query.lower() == "exit":
            break

        best_match = ""
        max_score = 0

        with open("vector_store.txt", "r") as vs:

            vs.seek(0)

            for line in vs:
                line_lower = line.lower()
                score = 0

                for word in query.lower().split():
                    if word in line_lower:
                        score += 1

                if score > max_score:
                    max_score = score
                    best_match = line.strip()

        print("Answer:", best_match if best_match else "No match found")
