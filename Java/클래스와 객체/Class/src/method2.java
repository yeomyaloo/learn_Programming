
public class method2 {
	
	
	public static void main(String[] args) {
		// class가 가진 메소드를 사용하기 위해서는 객체로 만들어야 사용할 수 있다.
		
		method1 myclass = new method1();
		// 사용할 클래스명 / 내가 이 클래스명을 다시 쓸 이름 = new 사용할 클래스명();
		
		myclass.method1_1();
		myclass.method1_2(10);
		
		int value = myclass.method1_3();
		System.out.println("m3이 리턴한 값" + value);
		
		myclass.method1_4(5, 10);
		
		int value2 = myclass.method1_5(55);
		System.out.println("m5이 리턴한 값" + value2);
				
	}
}
