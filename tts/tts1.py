# 먼저 gTTS 라이브러리를 설치해야 합니다.
# 설치 명령: pip install gTTS playsound

from gtts import gTTS
from playsound import playsound

# TTS로 변환할 문구 (사용자가 듣고 싶은 텍스트)
text = """
멀티클라우드(Multi-Cloud)
예상문제 1: 멀티클라우드(Multi-Cloud)의 개념을 정의하고, 이를 활용하는 기업의 주요 이점을 1~2가지 서술하시오.
예시답변: 멀티클라우드는 두 개 이상의 서로 다른 클라우드 서비스 제공업체(예: AWS, Azure, GCP)의 인프라나 서비스를 동시에 사용하는 전략을 의미한다. 이를 통해 특정 벤더에 대한 종속성(Vendor Lock-in)을 감소시키며, 서로 다른 클라우드의 장점을 조합해 성능, 비용 최적화, 지역별 가용성 확대와 같은 이점을 얻을 수 있다.

예상문제 2: 멀티클라우드와 하이브리드 클라우드의 차이점을 간략히 설명하시오.
예시답변: 하이브리드 클라우드는 퍼블릭 클라우드와 온프레미스(프라이빗) 인프라를 결합한 환경을 말하는 반면, 멀티클라우드는 둘 이상의 퍼블릭 클라우드 제공업체 서비스들을 조합해 사용하는 전략이다. 즉, 하이브리드는 퍼블릭-프라이빗 혼합, 멀티클라우드는 퍼블릭-퍼블릭 혼합에 초점을 둔다.

클라우드 네이티브(Cloud Native)
예상문제 1: 클라우드 네이티브 애플리케이션의 주요 특징을 2~3가지 서술하시오.
예시답변: 클라우드 네이티브 애플리케이션은 컨테이너화, 마이크로서비스 아키텍처, 동적 오케스트레이션(Kubernetes 등), DevOps 문화 및 CI/CD 파이프라인을 통해 신속한 배포와 확장성, 탄력성을 갖추는 특징을 가진다.

예상문제 2: 클라우드 네이티브 애플리케이션과 전통적 모놀리식 애플리케이션의 차이를 한 가지 관점(배포, 확장, 유지보수 중 택1)에서 설명하시오.
예시답변: 배포 관점에서 클라우드 네이티브 애플리케이션은 마이크로서비스 단위로 독립적으로 배포가 가능하므로 새로운 기능 추가나 수정 시 전체 애플리케이션 재배포 없이 특정 서비스만 업데이트가 가능하다. 반면 전통적 모놀리식 애플리케이션은 하나의 커다란 애플리케이션으로 묶여 있어 배포 시 전체를 재구축 및 재배포 해야 한다.

도커(Docker)
예상문제 1: Docker를 이용한 컨테이너 기반 가상화와 전통적인 가상머신(VM) 기반 가상화의 차이점을 서술하시오.
예시답변: VM은 하이퍼바이저 위에서 게스트 OS를 포함한 무거운 환경을 제공하지만, Docker 컨테이너는 호스트 OS 커널을 공유하는 경량 프로세스 격리 방식으로 실행된다. 이로 인해 컨테이너는 VM보다 시작 속도가 빠르고 자원 소모가 적어 효율적인 배포와 확장이 가능하다.

예상문제 2: Docker 이미지(Docker Image)와 Docker 컨테이너(Docker Container)의 차이를 설명하시오.
예시답변: Docker 이미지는 컨테이너 실행을 위한 읽기 전용 템플릿이며, 특정 애플리케이션과 해당 환경 구성을 담고 있다. Docker 컨테이너는 이러한 이미지를 실행한 상태로, 실제 애플리케이션이 동작하는 가상화된 런타임 환경이다.

DevOps
예상문제 1: DevOps 문화가 전통적인 개발(Dev)과 운영(Ops) 조직 구조와 방식에 가져온 변화를 1~2가지 서술하시오.
예시답변: DevOps는 개발팀과 운영팀 사이의 경계를 허물어 협업을 강화하고, 지속적 통합(CI)과 지속적 배포(CD) 파이프라인을 통해 소프트웨어 업데이트 주기와 품질을 개선한다. 이로써 빈번하고 안정적인 릴리스를 달성하며, 조직 전체의 민첩성을 높인다.

예상문제 2: DevOps 환경에서 CI/CD 파이프라인이 갖는 의미를 설명하시오.
예시답변: CI/CD 파이프라인은 소스 코드 변경이 발생할 때마다 자동으로 빌드, 테스트, 배포 과정을 실행하는 워크플로우를 뜻한다. 이는 인적 개입을 최소화하고, 코드 품질을 유지하며, 빠르고 안정적인 릴리스로 비즈니스 가치를 신속히 제공한다.

MSA(Microservices Architecture)
예상문제 1: 마이크로서비스 아키텍처(MSA)의 정의와 모놀리식(monolithic) 아키텍처와의 주요 차이점을 서술하시오.
예시답변: MSA는 애플리케이션을 작은 단위의 독립적인 서비스로 나누어 각각 독립적으로 배포, 확장, 유지보수하는 아키텍처 방식이다. 모놀리식에 비해 서비스별로 스케일링이 용이하고 장애 격리가 수월하며, 기능 개선 및 업데이트 주기가 짧다.

예상문제 2: MSA 구현 시 고려해야 할 과제나 어려움 두 가지를 서술하시오.
예시답변: 첫째, 서비스 간 통신 및 서비스 디스커버리 관리가 필요하여 네트워크 복잡성이 증가한다. 둘째, 로그 및 모니터링 체계 확립이 필수적이며, 이는 분산 환경에서 각 서비스별 메트릭 수집과 분석을 어렵게 만든다.

가상화(Virtualization)
예상문제 1: 가상화(Virtualization)의 기본 개념과 이를 통해 얻을 수 있는 대표적인 이점 1~2가지를 서술하시오.
예시답변: 가상화는 물리적 하드웨어 리소스를 추상화하여 하나의 물리 서버에서 여러 가상 머신을 실행하는 기술이다. 이를 통해 서버 자원의 활용도를 높이고, 애플리케이션 격리 및 이식성을 확보하며, 인프라 관리의 유연성을 제공한다.

예상문제 2: 하이퍼바이저(Hypervisor)의 역할을 간략히 설명하시오.
예시답변: 하이퍼바이저는 물리적 하드웨어 리소스를 추상화하여 여러 가상 머신에 할당하고, 이들 VM을 관리하는 소프트웨어 계층이다. 이를 통해 서로 다른 VM들이 독립된 환경에서 동시에 동작할 수 있도록 지원한다.
"""

# 음성 합성 (한국어 TTS)
tts = gTTS(text=text, lang='ko')

# mp3 파일로 저장
tts.save("example_tts.mp3")

# 저장한 mp3 재생
playsound("example_tts.mp3")
