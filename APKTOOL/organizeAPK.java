// executing commands on cmd prompt 
import java.io.File;
import java.util.Scanner;
import java.nio.file.Paths;

public class organizeAPK { 
    public static void main(String[] args) { 

        System.out.println("Running");

        String decompileDir="decompiled/"; //location of decompiled APK files
        String passCommand=" ";

        Runtime runtime= Runtime.getRuntime(); //to run command prompt
         
         //get path to folder with downloaded APK files to get file list

        String dir=Paths.get(".").toAbsolutePath().normalize().toString(); //current folder, where decompile outputs are
        
        parseFiles parse= new parseFiles(dir); //get dir to APK files from googleplay
        File[] apkList= parse.getDirList(); //list of APK files from googleplay


        System.out.println("number of files " +apkList.length);
        
        //go through list, get file names, plug into command and decompile files 
        for(int i=0; i<apkList.length; i++){
            if( apkList[i].getName()!= "apktool.bat" || apkList[i].getName()!= "apktool.jar" || 
                       apkList[i].getName()!= "decompileAPK.java" || apkList[i].getName()!= "decompileAPK.class"
                       ||apkList[i].getName()!= "parseFiles.java" || apkList[i].getName()!= "parseFiles.class" 
                       ||apkList[i].getName()!= "organizeAPK.java" || apkList[i].getName()!= "organizeAPK.class")  {

                passCommand= "cmd /c cmd.exe /K \" "+apkList[i].getName();

                System.out.println(passCommand);
            }
            
            
            // try
            // {  
            //  // format: runtime.exec("cmd /c start cmd.exe /K \" java -jar apktool.jar d apk2/com.mcdonalds.app_0_apps.evozi.com.zip");
            //  runtime.exec(passCommand);
            // } 
            // catch (Exception e) 
            // { 
            //     System.out.println("Error decompiling " +passCommand); 
            //     e.printStackTrace(); 
            // } 
            
        }
   
        
        }

        
} 