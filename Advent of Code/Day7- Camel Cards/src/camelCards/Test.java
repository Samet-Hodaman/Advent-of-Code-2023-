package camelCards;

import camelCards.entities.abstracts.TypeOfHands;

public class Test {

	public static void main(String[] args) {
		TypeOfHands five = TypeOfHands.FIVE_OF_A_KIND;
		TypeOfHands four = TypeOfHands.FOUR_OF_A_KIND;
		TypeOfHands three = TypeOfHands.THREE_OF_A_KIND;
		System.out.println(three.hasMorePriorityThan(four));
		

	}

}
