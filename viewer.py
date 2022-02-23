import os
from simple_chalk import chalk
import time
from tqdm import tqdm
import shutil

class Viewer:
    def view(fileName):
        try:
            file = open(fileName, "r")
        except FileNotFoundError:
            print(chalk.red("\nFile does not exist\n"))
            os._exit(1)
        else:
            pass

        # * Interface of Viewer viewing the file
        os.system("cls")
        print(fileName.center(150))
        print("_" * 145)
        print("\n")

        # * Main Functions
        numberOfLines = 0
        for line in file:
            data = line.__str__()
            numberOfLines = numberOfLines + 1
            print(str(numberOfLines) + " | " + data)

        print("\n")
        print("_" * 145)
        print("Press Ctrl + c to exit")
        try:
            stop = input()
        except KeyboardInterrupt:
            print("\nViewer Closed\n")
            os._exit(0)

        return

    def copier(fileName, logo):
        nowPath = os.getcwd()
        try:
            file = open(fileName, "r")
        except FileNotFoundError:
            print(chalk.red("\nFile does not exist\n"))
            os._exit(1)
        else:
            pass
        givenFileData = file.read()

        # print(fileName.center(100))
        # print("_" * 145)
        print(
            "\nConform you want to copy this file content to another file (Copy paste method)."
        )
        conformation = input("conform [Yy , Nn]: ")
        if conformation == "Y":
            pass
        elif conformation == "y":
            pass
        elif conformation == "N":
            os._exit(0)
        elif conformation == "n":
            os._exit(0)
        else:
            print("You entered a invalid value.")
            os._exit(0)

        # * Interface of Copier
        os.system("cls")
        print("\n\nYour original file is : ", fileName)

        print(
            "\nEnter the name of the file . Where you want to paste the data , enter below"
        )
        try:
            pasteFileName = input("Enter File name : ")
        except KeyboardInterrupt:
            print(chalk.yellow("User Exited"))
            os._exit(1)
        except ValueError:
            print("Error , unreadable file input.")
            os._exit(1)

        print(
            "\nEnter the name of folder or paste the path to save your copied file there , enter below"
        )
        try:
            whereSaveFile = input("Enter Folder name or Path : ")
        except KeyboardInterrupt:
            print(chalk.yellow("User Exited"))
            os._exit(1)
        except ValueError:
            print("Error , unreadable file input.")
            os._exit(1)
        print("\n")

        # * File Creating Interface
        print("Creating file ...")
        for i in tqdm(range(100), desc="Creating… ", ascii=False, ncols=100):
            time.sleep(0.02)
        copingFile = open(pasteFileName, "w")
        print(chalk.green("File has created."))
        print("\n")

        # * File coping Interface
        print("Coping content from " + fileName + " to " + pasteFileName)
        print("\nCoping ...")
        for i in tqdm(range(100), desc="Transfering… ", ascii=False, ncols=100):
            time.sleep(0.02)
        copingFile.write(
            givenFileData
            + "\n\nThis file is copied using Terminal File Viewer.\n"
            + logo
        )
        print(chalk.green("Files Data has Transferred."))
        print("\n")
        copingFile.close()

        # * File transfering to selected folder
        print("Transfering your copied file to your selected path : " + whereSaveFile)
        print("\nTransfering ...")
        for i in tqdm(range(100), desc="Transfering… ", ascii=False, ncols=100):
            time.sleep(0.02)
        shutil.move(nowPath+"/"+pasteFileName,nowPath+"/"+whereSaveFile)
        print(chalk.green("Saved"))
        print("\n")
        print(chalk.green("Your File is saved at "),nowPath+"/"+whereSaveFile)

    def error():
        print("Something Went Wrong!")
        os._exit(1)
