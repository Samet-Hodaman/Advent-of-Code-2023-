package camelCards.dataAccess;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

import camelCards.entities.abstracts.Hand;
import camelCards.entities.concretes.FiveOfAKind;
import camelCards.entities.concretes.FourOfAKind;
import camelCards.entities.concretes.FullHouse;
import camelCards.entities.concretes.HighCard;
import camelCards.entities.concretes.OnePair;
import camelCards.entities.concretes.ThreeOfAKind;
import camelCards.entities.concretes.TwoPair;
import camelCards.utils.FileIO;

public class CardsDao {
	public static final HashMap<Character, Integer> VALUES_OF = getValuesOfHashMap();
	
	public CardsDao() {
		
	}
	
	private static HashMap<Character, Integer> getValuesOfHashMap(){
		HashMap<Character, Integer> valuesHashMap = new HashMap<>();
		valuesHashMap.put('2', 2);
		valuesHashMap.put('3', 3);
		valuesHashMap.put('4', 4);
		valuesHashMap.put('5', 5);
		valuesHashMap.put('6', 6);
		valuesHashMap.put('7', 7);
		valuesHashMap.put('8', 8);
		valuesHashMap.put('9', 9);
		valuesHashMap.put('T', 10);
		valuesHashMap.put('J', 1);	// 11
		valuesHashMap.put('Q', 11);
		valuesHashMap.put('K', 12);
		valuesHashMap.put('A', 13);
		return valuesHashMap;
	}
	
	public ArrayList<Hand> getHandsArrayList(){
		ArrayList<Hand> handsArrayList = new ArrayList<>();
		ArrayList<String> linesStringArrayList = FileIO.readFile("resources/inputs.txt");
		for(int i=0; i<linesStringArrayList.size(); i++) {
			StringTokenizer stringTokenizer = new StringTokenizer(linesStringArrayList.get(i)," ");
			String cardsString = stringTokenizer.nextToken();
			int offerPrice = Integer.valueOf(stringTokenizer.nextToken());
			handsArrayList.add(handGenerator(cardsString, offerPrice));
		}
		return handsArrayList;
	}
	
	public static Hand handGenerator(String cards, int offerPrice) {
		HashMap<Character, Integer> hashMap = new HashMap<>();
		for(char c : cards.toCharArray()) {
			if(hashMap.containsKey(c)) {
				int v = hashMap.get(c);
				hashMap.replace(c, v,v+1);
			} else
				hashMap.put(c, 1);
		}

		ArrayList<Character> charArrayList;
		int size = hashMap.size();
		switch(size) {
			case 5: // high card
				HighCard highCard = new HighCard(offerPrice);
				charArrayList = new ArrayList<>();
				for(char c : hashMap.keySet())
					charArrayList.add(c);
				charArrayList = sortArrayList(charArrayList);
				highCard.setFirst(charArrayList.get(0));
				highCard.setSecond(charArrayList.get(1));
				highCard.setThird(charArrayList.get(2));
				highCard.setForth(charArrayList.get(3));
				highCard.setFifth(charArrayList.get(4));
				highCard.setCardString(cards);
				return highCard;
			case 4: // one pair
				OnePair onePair = new OnePair(offerPrice);
				charArrayList = new ArrayList<>();
				for(char c:hashMap.keySet()) {
					if(hashMap.get(c) == 2)
						onePair.setValueOfPair(c);
					else
						charArrayList.add(c);
				}
				charArrayList = sortArrayList(charArrayList);
				onePair.setFirst(charArrayList.get(0));
				onePair.setSecond(charArrayList.get(1));
				onePair.setThird(charArrayList.get(2));
				onePair.setCardString(cards);
				return onePair;
			case 3: // three of a kind or two pair
				if(hashMap.containsValue(3)) { // three of a kind
					ThreeOfAKind threeOfAKind = new ThreeOfAKind(offerPrice);
					charArrayList = new ArrayList<>();
					for(char c:hashMap.keySet()) {
						if(hashMap.get(c) == 3)
							threeOfAKind.setValueOfThree(c);
						charArrayList.add(c);
					}
					charArrayList = sortArrayList(charArrayList);
					threeOfAKind.setFirst(charArrayList.get(0));
					threeOfAKind.setSecond(charArrayList.get(1));
					threeOfAKind.setCardString(cards);
					return threeOfAKind;
				} else { // two pair
					TwoPair twoPair = new TwoPair(offerPrice);
					charArrayList = new ArrayList<>();
					for(char c:hashMap.keySet()) {
						if(hashMap.get(c) == 1)
							twoPair.setFirst(c);
						else
							charArrayList.add(c);							
					}
					charArrayList = sortArrayList(charArrayList);
					twoPair.setValueOfFirstPair(charArrayList.get(0));
					twoPair.setValueOfSecondPair(charArrayList.get(1));
					twoPair.setCardString(cards);
					return twoPair;
				}
			case 2:	// four of a kind or full house
				if(hashMap.containsValue(1) && hashMap.containsValue(4)) { // four of a kind
					FourOfAKind fourOfAKind = new FourOfAKind(offerPrice);
					for(char c:hashMap.keySet()) {
						if(hashMap.get(c) == 4)
							fourOfAKind.setValueOfFour(c);
						else
							fourOfAKind.setFirst(c);			
					}
					fourOfAKind.setCardString(cards);
					return fourOfAKind;
				} else { // full house
					FullHouse fullHouse = new FullHouse(offerPrice);
					for(char c:hashMap.keySet()) {
						if(hashMap.get(c) == 3)
							fullHouse.setValueOfThree(c);
						else
							fullHouse.setValueOfTwo(c);
					}
					fullHouse.setCardString(cards);
					return fullHouse;
				}
			case 1: // five of a kind
				FiveOfAKind fiveOfAKind = new FiveOfAKind(offerPrice);
				for(char c:hashMap.keySet())
					fiveOfAKind.setValueOfFive(c);
				fiveOfAKind.setCardString(cards);
				return fiveOfAKind;
			default:
				throw new IllegalStateException("Unexpected state.");
		}
	}
	
	private static ArrayList<Character> sortArrayList(ArrayList<Character> charArrayList){
		
		ArrayList<Character> temp = new ArrayList<>(charArrayList);
		ArrayList<Character> sortedArrayList = new ArrayList<>();

		while(!temp.isEmpty()) {
			Character maxChar = temp.get(0);
			for(int i=0; i<temp.size(); i++) {
				Character other = temp.get(i);
				if(VALUES_OF.get(other) > VALUES_OF.get(maxChar))
					maxChar = other;
			}
			if(temp.remove(maxChar))
			sortedArrayList.add(maxChar);
		}
		return sortedArrayList;
	}
	public static int compareCards(char c1, char c2) {
		int val1 = VALUES_OF.get(c1);
		int val2 = VALUES_OF.get(c2);
		if(val1 > val2)
			return 1;
		else if (val1 < val2)
			return -1;
		else
			return 0;
	}

}
