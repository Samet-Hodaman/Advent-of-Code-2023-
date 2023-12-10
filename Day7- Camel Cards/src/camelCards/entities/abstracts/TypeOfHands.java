package camelCards.entities.abstracts;

public enum TypeOfHands {
	FIVE_OF_A_KIND(6),
	FOUR_OF_A_KIND(5),
	FULL_HOUSE(4),
	THREE_OF_A_KIND(3),
	TWO_PAIR(2),
	ONE_PAIR(1),
	HIGH_CARD(0);
	private Integer precedence;
	
	private TypeOfHands(int precedence) {
		this.precedence = precedence;
	}
	public int hasMorePriorityThan(TypeOfHands other) {
		if(this.precedence > other.precedence)
			return 1;
		else if(this.precedence == other.precedence)
			return 0;
		else
			return -1;
	}
}
