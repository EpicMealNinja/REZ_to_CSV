import os
import PyPDF2
import PySimpleGUI as sg

#define main function
def main():
    #using PySimpleGUI find the folder with exports and pdfs
    layout = [[sg.Text("Select folder of pdfs (Will work with all the pdfs in the folder)")],
                [sg.Input(), sg.FolderBrowse()],
                [sg.Button("Ok")]]
    window = sg.Window("Folder Browser", layout)
    event, values = window.read()
    window.close()
    #get the path of the selected folder
    path = values[0]
    #get a list of all the files in the directory
    

    #create a folder to store the csv files
    #loop through the list of files





if __name__ == "__main__":
    main()