import glob
import subprocess


def main():
    for d in glob.glob("./src/*.gv"):
        graph_name = d.split("/")[-1].split(".")[0]
        subprocess.run(["dot", "-Tpdf", d, "-o", f"./out/{graph_name}.pdf"])
        subprocess.run(
            ["dot", "-Tpng", "-Gdpi=300", d, "-o", f"./out/{graph_name}.png"]
        )


if __name__ == "__main__":
    main()
