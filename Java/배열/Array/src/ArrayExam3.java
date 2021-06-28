
public class ArrayExam3 {
//2차원 배열 =배열의 배열
	public static void main(String[] args) {
		int [][] array4 = new int[3][4]; //3행 4열
		//array4 = 이차원 배열을 가르키는 변수 
		array4[0][0] = 10; // array4[0] =10인 경우엔 참조하는 것에 값을 부여하는 것이라 안 됨
		
		int [][] array5= new int[3][];
		array5[0] = new int[1]; //2. 값을 넣으려면 크기를 지정해주어야 한다. 
		
		//1. array5[0][0] = 10; 이것도 오류 값을 실제로 줘야 오류 ㄴ 
		array5[0][0] = 10;
		
		// 2차원 배열의 선언과 동시에 초기화 하는 방법
		int[][] array6 = {{1},{1,2},{1,2,3}};
		
	
		System.out.println(array6[0][0]);
	
		
		
			
	}

}
