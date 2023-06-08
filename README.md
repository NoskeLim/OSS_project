# 프로젝트 배경
동아리 내의 소통 창구이자 지속적이고 끝임 없는 관리를 위하여 만든 웹사이트이다.

## 제공기능
총 3가지 기능을 제공한다. 
1.게시글을 업로드 할 수 있는 Post
2.같은 동아리의 부원들을 확인할 수 있는 Members
3.자신의 정보를 조회할 수 있는 My Information이 있다.
 
### POST
게시글 업로드를 통하여 동아리 부원들 혹은 필요한 공지 사항이 있을 때 확인할 수 있는 기능이며 계속적인 소통을 가능하게 한다.

### MEMBERS
동아리에 가입되어 있는 사람의 경우 다른 사람의 나이, 아이디 (혹은 이름), 이메일, 거주지 등을 조회할 수 있으며 오프라인에서의 소통도 가능하게 할 수 있다.

#### MY INFORMATION
자신의 정보를 조회할 수 있으며 변경 가능하다.

##### 시스템 구조 및 설계
Index.html은 곧 메인 페이지를 담당한다. 
위의 기능 3가지를 각각 다른 버튼으로 구현하여 각 기능을 담당하게 한다. 
오른쪽 위의 배너는 navigate를 활용하여 Log In, Registration, My Information, Contact가 가능하
모든 구성은 외부 Template소스코드의 html과 css로 구성하였고 css의 확장판인 scss도 같이 연동하여 구현하게 하였다. 
Web Framework를 담당하는 Django와 Flask 중 Flask를 선택하게 된 이유는 Flask는 Django에 비하여 더 가볍고 심플한 Framework를 지향하기 때문에 
위 프로젝트를 구성하는 데에 있어서 더 적합하여 선택하게 되었다. 이에 더하여 REST API 서버처럼 요청과 응답이 매우 확정적이기 때문에 효율적이라고 생각하였다.
이 웹프로그램의 Back-End는 많은 Data나 서버에 대한 요청이 많지 않으므로 Pyhton으로 구성하여 빠르고 효율적인 프로그램을 구성하도록 하였다.

