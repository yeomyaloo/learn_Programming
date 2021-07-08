
public class CarExam2 {
	
	public static void main(String[] args) {
//		Car c1 = new Car();
		// 카 객체를 만들면 기본생성자를 이용해서 생성자를 만들 수 없다.
		Car c2 = new Car("소방차");
		Car c3 = new Car("구급차");
		System.out.println(c2.name);
	}
	
}
