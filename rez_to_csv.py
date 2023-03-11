import os
import PyPDF2
import PySimpleGUI as sg

#define main function
def main():
    #using PySimpleGUI find the folder with exports and pdfs
    layout = [[sg.Text("Select folder with exports and pdfs")],
                [sg.Input(), sg.FolderBrowse()],
                [sg.Button("Ok")]]
    window = sg.Window("Folder Browser", layout)
    event, values = window.read()
    window.close()
    #get the path of the selected folder
    path = values[0]
    #get the list of files in the folder
    list_of_files = os.listdir(path)

    #Get the pdf file and the chunk file
    pdfFile = ""
    chunkFile = open("export/chunk.csv", "r")
    #loop through the list of files
    for file in list_of_files:
        if file.endswith(".pdf"):
            pdfFile = file
    pdfReader = PyPDF2.PdfReader(pdfFile)
    







if __name__ == "__main__":
    main()