package javaStandard;

class Card {
	
	final int NUMBER;
	final String KIND;
	final int width = 100;
	final int height = 250;
	
	Card(String kind, int num){
		KIND = kind;
		NUMBER = num;
	}
	
	Card(){
		this("HEART",1);
	}
	
	public String toString() {
		return "" + KIND + " "+NUMBER;
	}


public static void main(String args[]) {
	Card c = new Card("HEART",10);
	System.out.println(c.KIND);
	System.out.println(c.NUMBER);
	} 
}