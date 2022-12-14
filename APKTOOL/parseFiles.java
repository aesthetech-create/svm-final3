import java.io.File;
import java.util.Scanner;

public class parseFiles{
	String directoryPath="";//set path here
	File dir;
	File [] dirList;

	//set dir and dirlist

    public parseFiles(String pathLink){
    	
    	this.directoryPath=pathLink;
    	System.out.println("from directory "+ pathLink);
    	
    	this.dir= new File(directoryPath); //initialize file with path
    	this.dirList= dir.listFiles(); //list of files in path
    	
    }

    public File[] getDirList(){
    	return dirList;
    }
    
    //iterate through list
    


	//read file can turn to text to pass to python code


    //move folder to other folder

    //delete/clear folder
}