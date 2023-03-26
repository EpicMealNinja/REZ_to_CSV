import os
import PyPDF2
import PySimpleGUI as sg

#define main function
def main():
    #using PySimpleGUI find the folder with files to be converted
    layout = [[sg.Text("Select folder with files to be converted")],
                [sg.Input(), sg.FolderBrowse()],
                [sg.Button("Ok")]]
    window = sg.Window("Folder Browser", layout)
    event, values = window.read()
    window.close()
    #get the path of the selected folder
    path = values[0]
    #get the list of files in the folder
    list_of_folders = os.listdir(path)

    #loop through the list of folders
    for folder in list_of_folders:
        list_of_files = os.listdir(path + "/" + folder)
        #loop through the list of files
        for file in list_of_files:
            #if the files begins with "AAHP" then open the file
            if file.startswith("AAHP"):
                file_name = file
                #Open the csv file with utf-8 encoding
                transript_file = open(path + "/" + folder + "/" + file, "r", encoding="utf-8")
                #read the file
                transcript = transript_file.read()
                #close the file
                transript_file.close()
            if file == "chunk.csv":
                #open the csv file with utf-8 encoding
                chunk_file = open(path + "/" + folder + "/" + file, "r", encoding="utf-8")
                #read the file
                chunk = chunk_file.read()
                #close the file
                chunk_file.close()
        #Make changes to the transcript file to match output desired
        #Split the transcript file into a list
        transcript_list = transcript.split("\n")
        #Replace the first line of the transcript file
        transcript_list[0] = "Text, Chunk, Feature"

        #Split the chunk file into a list
        chunk_list = chunk.split("\n")
        #Remove the first line of the chunk file
        chunk_list.pop(0)

        #Make a folder to store output files in at .py file location
        if not os.path.exists("output"):
            os.mkdir("output")
        #create a file to write all outputs to in the output folder
        output_file = open("output/" + file_name + ".csv", "w", encoding="utf-8")

        #loop through the list of lines in the transcript file
        for line in transcript_list:
            #If the line contains a chunk then put the chunk in the next column
            for chunk in chunk_list:
                #Split the chunk into a list
                chunk_split = chunk.split(",")
                print(chunk_split)
                #If the line contains the chunk then put the chunk in the next column
                if chunk_split[2] in line:
                    line = line + "," + chunk_split[2]
                    #If the line contains the feature then put the feature in the next column
                    for i in range(3, len(chunk_split)):
                        if chunk_split[i] != "":
                            line = line + "," + chunk_split[i]
            #Write the line to the output file
            output_file.write(line + "\n")
        #Close the output file
        output_file.close()
                
    







if __name__ == "__main__":
    main()