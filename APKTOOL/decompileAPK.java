// executing commands on cmd prompt 
import java.io.File;
import java.nio.file.Paths;

public class decompileAPK { 
    public static void main(String[] args) { 

        System.out.println("Running");


        String apkDir= "APKTOOL\\apkGooglePlayFiles\\"; //location of downloaded APK files
        String decompileCommand="java -jar apktool.jar \" d"; //command used to decompile apk files in terminal
        String passCommand=" ";

        Runtime runtime= Runtime.getRuntime(); //to run command prompt
         
         //get path to folder with downloaded APK files to get file list

        String dir=Paths.get(".").toAbsolutePath().normalize().toString()+File.separator +apkDir; 
        
        parseFiles parse= new parseFiles(dir); //get dir to APK files from googleplay
        File[] apkList= parse.getDirList(); //list of APK files from googleplay


        System.out.println("number of files" + apkList.length);
        
        //go through list, get file names, plug into command and decompile files 
        for(int i=0; i<apkList.length; i++){
            // decompileCommand = "java -jar apktool.jar -f -o \"" + outDir + File.separator + apkList[i].getName() + "\" d";
            passCommand= "cmd /c cmd.exe /K \" "+ decompileCommand + " " + apkDir + apkList[i].getName() ;
            Process proc = null;
            try
            {  
             // format: runtime.exec("cmd /c start cmd.exe /K  " java -jar apktool.jar d apk2/com.mcdonalds.app_0_apps.evozi.com.zip");
            runtime.exec(passCommand);
            System.out.println(i + ": " + passCommand);

            } 
            catch (Exception e) 
            { 
                System.out.println("Error decompiling " +passCommand); 
                e.printStackTrace(); 
            }

            
        }
    }
} 