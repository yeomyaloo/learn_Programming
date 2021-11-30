package javajungsuk;


//부모
class Product2{
	int price;//제품가격
	int bonusPoint;//보너스점수
	
	Product2(int price){
		this.price = price;
		bonusPoint = (int)(price/10.0); //보너스 점수는 제품 가격의 10%
	}
}


//자손
class Tv2 extends Product2 {
	Tv2(){
		//조상 클래스의 생성자 Product2(int price)를 호출
		super(100); //Tv 가격 100만원으로 설정
	}
	public String toString() {
		return "Tv";
		}
}
class Computer2 extends Product2 {
	Computer2() {
		super(200);
	}
	public String toString() { 
		return "Computer"; 
		}
}
class Audio2 extends Product2 {
	Audio2(){ 
		super(50); 
	}
	public String toString() {
		return "Audio";
	}
}

class Buyer2 { //물건을 사는 사람
	int money = 1000; //소유금액
	int bonusPoint = 0; //보너스점수
	Product2[] cart = new Product2[10]; //구입제품 저장하기 위한 배열
	int i = 0; // Product 배열에 사용될 카운터
	
	
	void buy(Product2 p) {
		if (money < p.price) {
			System.out.println("잔액이 부족하여 물건을 살 수 없습니다.");
			return;
		}
		
		money -= p.price;
		bonusPoint += p.bonusPoint;
		cart[i++] = p;
		System.out.println(p.toString() + "을/를 구입하셨습니다.");
	}
	void summary() {
		int sum = 0;
		String itemlist = "";
		
		for(int i = 0; i < cart.length; i++) {
			if(cart[i]==null) break;
			sum += cart[i].price;
			itemlist += cart[i] +", ";
		}
		System.out.println("구입하신 물품의 총금액은" + sum +"만원입니다.");
		System.out.println("구입하신 제품은" +itemlist +"입니다.");
		}
}


class java7_6_1{
	public static void main(String args[]) {
		Buyer2 b = new Buyer2();
		
		b.buy(new Tv2());
		b.buy(new Computer2());
		b.buy(new Audio2());
		b.summary();
		
	}
	
}
