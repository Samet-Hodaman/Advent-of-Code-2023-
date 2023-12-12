package camelCards.utils;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class FileIO {
	public static ArrayList<String> readFile(String pathName){
		ArrayList<String> readLines = new ArrayList<>();
		try {
			String lineString;
			BufferedReader bufferedReader = new BufferedReader(new FileReader(pathName));			
			while((lineString = bufferedReader.readLine()) != null) {
				lineString = lineString.replace("\uFEFF", "");	// removing BOM (Byte Order Mark) from the string.
				readLines.add(lineString);
			}
			bufferedReader.close();
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage()+" Check file path.");
		} catch (IOException e) {
			System.out.println(e.getMessage()+" ReadLine could not be working or file cannot be closed!");
		}
		return readLines;
	}
}
