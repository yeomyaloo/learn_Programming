
public class enum_1 {
	public static final String MALE ="MALE";
	public static final String FEMALE ="FEMALE";
	public static void main(String[] args) {
		// 열거타입을 선언해서 변수 선언할 때 변수타입으로 사용할 수 있다.
		String gender1;
		gender1 = enum_1.MALE;
		gender1 = enum_1.FEMALE;
		//두 개의 타입을 넣고 싶지만 메일 피메일 이외의 다른 스트링 타입이 들어갈 수 있다 이는 컴파일에는 문제가 생기지 않지만 그 이외에 문제가 생겨버린다.
		gender1 = "boy"; //이렇게 다른 스트링이 들어갈 수 있어서 이를 방지하기 위해 열거형 사용한다.
		
		
		
		Gender gender2;
		gender2 = Gender.MALE;
		gender2 = Gender.FEMALE;
//		gender2 = Gender.boy;  컴파일부터 오류가 나타난다.
		

	}

}
enum Gender{
	MALE, FEMALE;
}