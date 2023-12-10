package camelCards.entities.concretes;

import camelCards.entities.abstracts.Hand;
import camelCards.entities.abstracts.TypeOfHands;

public class OnePair extends Hand{
	private char valueOfPair;
	private char first;
	private char second;
	private char third;
	
	public OnePair(int offerPrice) {
		super(TypeOfHands.ONE_PAIR);
		super.setOfferPrice(offerPrice);
	}
	public OnePair(OnePair onePair) { // Copy Constructor
		super(onePair);
		this.valueOfPair = onePair.getValueOfPair();
		this.first = onePair.getFirst();
		this.second = onePair.getSecond();
		this.third = onePair.getThird();
	}
	
	public char getValueOfPair() {
		return valueOfPair;
	}
	public void setValueOfPair(char valueOfPair) {
		this.valueOfPair = valueOfPair;
	}
	public char getFirst() {
		return first;
	}
	public void setFirst(char first) {
		this.first = first;
	}
	public char getSecond() {
		return second;
	}
	public void setSecond(char second) {
		this.second = second;
	}
	public char getThird() {
		return third;
	}
	public void setThird(char third) {
		this.third = third;
	}
	@Override
	public Hand getjokerHand() {
		switch(getNumOfJ()) {
			case 0:
				return new OnePair(this);
			case 2:
				ThreeOfAKind threeOfAKind = new ThreeOfAKind(getOfferPrice());
				threeOfAKind.setValueOfThree(first);
				threeOfAKind.setFirst(second);
				threeOfAKind.setSecond(third);
				threeOfAKind.setCardString(getCardString().replaceAll("J", ""+first));
				return threeOfAKind;
			case 1:
				threeOfAKind = new ThreeOfAKind(getOfferPrice());
				threeOfAKind.setCardString(getCardString().replaceAll("J" , ""+valueOfPair));
				threeOfAKind.setValueOfThree(valueOfPair);
				threeOfAKind.setFirst((first == 'J') ? second : first);
				threeOfAKind.setSecond((second == 'J') ? third : second);
				return threeOfAKind;
			default:
				throw new IllegalStateException();
		}
	}	
}
