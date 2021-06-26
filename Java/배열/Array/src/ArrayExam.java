
public class ArrayExam {
	public static void main(String[] args) {
		
		//배열은 하나지만 값은 여러개 이기때문에 기본데이터 타입이 아니고 참조형데이터타입이다!!!
		//1차원 배열 
		
		int[] array1 = new int[100];
		//100개의 정수값을 저장할 수 있는 int형 배열 array1 생성 자바는 변수의 크기를 정해줘야 한다.
		
		array1[0] = 50;
		array1[10] = 100;
		
		//선언과 동시에 값까지 줄 수 있는 방법
		int[] array2 = new int[] {1,2,3,4};
		
		
		//new라는 코드 없이 선언과 동시에 값까지 부여하는 방법
		int[] array3 = {1,2,3,4};
		
		//값을 꺼내서 사용하는 방법
		System.out.println(array3[3]);
		
		
		//0번째 인덱스 값을 꺼내서 value라는 변수에 담아주세요
		int value = array3[0];
		
		//for문을 이용해서 값을 차례대로 꺼내거나 넣어주는 방법도 있다. 
	}

}
