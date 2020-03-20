# Motube Project

## 1. 개요

- 영화 추천 방법
- 개발환경
- Seed Data
- 소스코드



## 2. 영화 추천 방법

- 지난 1년 동안 박스오피스에 올라온 영화들을 기반으로, 유튜브에서의 화제성을 기준으로 영화를 추천해준다. 박스오피스 1위에 오른 영화라고 모두 같은 정도의 인기를 얻은 것은 아니다. 어떤 영화는 재밌다고 화제가 되지만, 어떤 영화는 반대의 이유로 화제가 된다. 어느 이유든 사람들의 관심을 끈 영화는 관련 컨텐츠들도 주목을 받기 마련이다. 최근 유튜브 플랫폼의 폭발적인 수요 증가로 유튜브의 인기 영상이 사람들의 주된 관심사일 정도로 그 영향력이 커졌다. 그러므로 유튜브에서 어떤 영화가 관련 영상을 많이 양산해냈다면 이 영화는 추천해줄 만 하다고 할 수 있다. 그래서 본 팀은 박스오피스에 올라왔던 200여개의 영화 중 유튜브에서의 화제성을 기준으로 영화를 추천하였다. 



## 3. 개발환경

코드는 다음의 환경에서 작성되었다.

- Python 3.7.4
- Django 2.2.4



만들어진 소스코드는 heroku를 통해 배포되었다. 주소는 다음과 같다. [Motube]( https://ssafy-create.herokuapp.com/ )

- 테스트 계정의 ID : testaccount

- 테스트 계정 비밀번호: qlalfqjsgh


다음의 패키지를 사용하였다.

- bootstrap 0.1.0
- django-bootstrap4 1.0.1
- django-extensions 2.2.5
- django-heroku 0.3.1
- django-pandas 0.6.1
- gunicorn 20.0.4
- ipython 7.10.0
- ipython-genutils 0.2.0
- numpy 1.17.4
- pandas 0.25.3
- parso 0.5.1
- pickleshare 0.7.5
- prompt-toolkit 3.0.0
- psycopg2 2.8.4
- Pygments 2.5.1
- python-dateutil 2.8.1
- python-decouple 3.3
- pytz 2019.3
- six 1.13.0
- soupsieve 1.9.5
- sqlparse 0.3.0
- traitlets 4.3.3
- wcwidth 0.1.7
- whitenoise 4.1.4



## 4. 데이터 구성

- DB에 넣은 영화 정보를 만들었다. 이는 영화진흥위원회 API와 네이버 영화 검색, 유튜브 API를 활용하였다.
- 만들어진 데이터는 크게 3종류다. 장르, 영화 정보, 유튜브 비디오에 대한 정보다.



### 1) 장르

```json
    {
        "pk": 1,
        "model": "movies.genre",
        "fields": {
            "name": "드라마"
        }
    },
```

필드는 pk와 이름 뿐이다.



### 2) 영화

```json
    {
        "pk": 1,
        "model": "movies.Movie",
        "fields": {
            "title": "겨울왕국 2",
            "open_date": "2019-11-21",
            "description": "<div class=\"story_area\">\n<div class=\"title_area\">\n<h4 class=\"h_story\"><strong class=\"blind\">줄거리</strong></h4>\n</div>\n<h5 class=\"h_tx_story\">내 마법의 힘은 어디서 왔을까?<br/>\r\n나를 부르는 저 목소리는 누구지?</h5>\n<p class=\"con_tx\">어느 날 부턴가 의문의 목소리가 엘사를 부르고, 평화로운 아렌델 왕국을 위협한다.\r<br/> 트롤은 모든 것은 과거에서 시작되었음을 알려주며 엘사의 힘의 비밀과 진실을 찾아 떠나야한다고 조언한다. \r<br/> \r<br/> 위험에 빠진 아렌델 왕국을 구해야만 하는 엘사와 안나는 숨겨진 과거의 진실을 찾아\r<br/> 크리스토프, 올라프 그리고 스벤과 함께 위험천만한 놀라운 모험을 떠나게 된다.\r<br/> 자신의 힘을 두려워했던 엘사는 이제 이 모험을 헤쳐나가기에 자신의 힘이 충분하다고 믿어야만 하는데…\r<br/> \r<br/> 두려움을 깨고 새로운 운명을 만나다!</p>\n</div>",
            "audi": 4437917,
            "rate": "전체 관람가",
            "naver_code": "136873",
            "poster": "https://movie-phinf.pstatic.net/20191121_221/1574298335357mqgLk_JPEG/movie_image.jpg",
            "genre": [
                15, 6, 11, 12, 2, 17
            ],
            "youtube_score": -0.08814831353396535
        }
    },
```

- 필드로는 제목, 개봉일, 소개, 관람객, 등급, 네이버 영화 코드, 포스터 URL, 장르, 유튜브 점수로 나눌 수 있다. 유튜브 점수는 자체 알고리즘을 사용하여 특정 영화 관련 유튜브 영상들의 조회수를 중심으로 데이터들의 분포도에 따른 가중치로 계산하였다. 값이 클수록 화제성이 높다. 



### 3) 유튜브 비디오

```json
    {
        "pk": 1,
        "model": "movies.Video",
        "fields": {
            "channelId": "UCpr2S3SBmyjvrx9Q4pLUZHw",
            "channelTitle": "movie trip 무비트립",
            "videoTitle": "영화 “겨울왕국2”의 비하인드 스토리",
            "description": "진짜 이번 겨울 극장가를 통으로 먹을 것 같은 \"겨울왕국2\" 여러분들의 의견을 댓글로 남겨주세요! #겨울왕국 #겨울왕국2 #비하인드 안녕하십니까...",
            "videoId": "WQI1lYtoxtM",
            "created_at": "2019-11-23T08:20:51.000Z",
            "thumbnail_small": "https://i.ytimg.com/vi/WQI1lYtoxtM/default.jpg",
            "thumbnail_medium": "https://i.ytimg.com/vi/WQI1lYtoxtM/mqdefault.jpg",
            "thumbnail_high": "https://i.ytimg.com/vi/WQI1lYtoxtM/hqdefault.jpg",
            "view_count": 221390,
            "like_count": 3103,
            "dislike_count": 69,
            "comment_count": 707,
            "video_src": "https://www.youtube.com/embed/WQI1lYtoxtM",
            "iframe": "<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/WQI1lYtoxtM\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>",
            "movie": 1
        }
    },
```

- 유튜브 API를 통해 받아온 정보를 필드로 저장하였다. 위의 사례는 겨울왕국을 유튜브에 검색하였을 때 나오는 첫번째 영상이다. 이때 view_count, like_count, dislike_count, comment_count 의 정보가 추천 알고리즘을 위한 점수를 구성하는데 데이터로 쓰였다. 차례대로 조회수, 좋아요 수, 싫어요 수, 댓글 수를 의미한다. 

- 각각 해당 영화를 유튜브에 검색했을 때 유튜브 알고리즘이 관련성이 높다고 판단하여 알려준 상위 10개의 동영상들을 기반으로 영화의 점수를 매겼다.



## 5. 소스코드

### 1) 디렉터리 구조

```
- motube
	-- templates
- accounts
	-- migrations
	-- templates
- movies
	-- fixture
		--- movies
	-- migrations
	-- templates
```

- 프로젝트 이름은 `motube` 이고 하부에 계정을 관리하는 `accounts`앱과 `movies`앱을 가진다.



### 2) motube

- templates 디렉터리를 통해 최상단의 `base.html` 파일을 구성하였다. 이후 만들어지는 페이지들은 이 파일을 상속한다.
- `settings.py` 를 통해 프로젝트 전반에 관한 설정을 하였다.

- `urls.py`를 통해 url을 통제하였는데, 계정 관련은 accounts 앱으로 보내주고, 영화 관리는 movies앱으로 보내줬다.

  ```python
  from django.contrib import admin
  from django.urls import path, include
  from movies import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('accounts/', include('accounts.urls')),
      path('movies/', include('movies.urls')),
      path('', views.index),
  ]
  ```

  

### 3) accounts

- 이 앱은 사용자의 계정을 관리한다. 로그인, 회원가입을 할 수 있다. 또한 개인이 특정 영화를 찜했을 때 찜한 목록을 확인할 수 있게 해주며, 유저들의 평점을 기반으로 만들어진 영화 추천 목록을 받을 수 있다.

- `templates`에는 2개의 페이지가 있다. 하나는 로그인과 회원가입이며, 다른 하나는 찜 목록을 보여주는 화면이다. 후자는 유저에 따라 다른 페이지를 보여준다.

- url은 다음과 같다.

  ```python
  from django.urls import path
  from . import views
  
  app_name = "accounts"
  urlpatterns = [
      path('', views.index, name='index'),
      path('<int:user_pk>/', views.user_detail, name="user_detail"),
      path('login/', views.login, name='login'),
      path('logout/', views.logout, name='logout'),
      path('signup/', views.signup, name='signup'),
      path('delete/', views.delete, name="delete"),
  ]
  
  ```

- view는 url 요청이 들어왔을 때 해당하는 정보를 전달해준다. 우리 앱에서 가장 특이한 부분은 detail을 보여주는 함수다.

  소스코드는 다음과 같다.

  ```python
  def user_detail(request, user_pk):
      person = get_object_or_404(get_user_model(), pk=user_pk)
      like_movies = person.like_movies.all()
      scores = Movie_Score.objects.all()
      if scores:
          ratings = scores.to_pivot_table(values='score', rows='movie', cols='user').to_dict()
          movie_names = get_recommend(ratings, request.user.username)
          movie_lst = []
          for name in movie_names:
              movie = Movie.objects.filter(title=name)[0]
              movie_lst.append(movie)
      else:
          movie_lst = []
      context = {
          'person': person,
          'like_movies': like_movies,
          "reco_movies": movie_lst
      }
      return render(request, 'accounts/detail.html', context=context)
  ```

  - 페이지를 랜더할 때, 유저가 좋아요한 영화들을 like_movies로 전달하였고, 추천 영화 목록을 reco_movies를 통해 전달했다.

  - `get_recommend`는 영화추천 알고리즘이다.

    코드는 다음과 같다.

    ```python
    def sim_pearson(data, name1, name2):
        sumX=0 # X의 합
        sumY=0 # Y의 합
        sumPowX=0 # X 제곱의 합
        sumPowY=0 # Y 제곱의 합
        sumXY=0 # X*Y의 합
        count=0 #영화 개수
        if not data.get(name1):
            return 0
        for i in data[name1]: # i = key
            if math.isnan(data[name1][i]):
                continue
            if math.isnan(data[name2][i]):
                continue
            # name1, name2 둘 다 관심있는 영화
            sumX+=data[name1][i]
            sumY+=data[name2][i]
            sumPowX+=pow(data[name1][i],2)
            sumPowY+=pow(data[name2][i],2)
            sumXY+=data[name1][i]*data[name2][i]
            count+=1
        
        if count == 0:
            return 0
        a = sumXY- ((sumX*sumY)/count)
        b = (sumPowX - (pow(sumX,2) / count))
        c = (sumPowY - (pow(sumY,2) / count))
        d = math.sqrt(b * c)
        if d == 0:
            return 0
        return a / d
    
    def top_match(data, name, index=3):
        li=[]
        for i in data: #딕셔너리를 돌고
            if name!=i: #자기 자신이 아닐때만
                li.append((sim_pearson(data,name,i),i)) #sim_function()을 통해 상관계수를 구하고 li[]에 추가
        li.sort() #오름차순
        li.reverse() #내림차순
        return li[:index]
    
    def get_recommend(data, person):
        if not data.get(person):
            return []
        res = top_match(data, person)
        if not res:
            return []
        sim_person = max(res)[1]
        lst = []
        for movie in data[sim_person]:
            if math.isnan(data[sim_person][movie]):
                continue
            if math.isnan(data[person][movie]):
                lst.append(movie)
    
        return lst[:4]
    ```

    



### 4) movies

- 이 앱은 전체 영화 정보를 보여준다. 영화들은  추천 알고리즘을 통해 만들어진 점수를 기반으로 내림차순의 형태로`index.html`에 보여진다. 특정 영화를 클릭하면 `detail.html`에서 해당 영화의 상세 정보를 파악할 수 있다. 영화 제목을 기반으로 검색도 가능한데, 그 결과는 `search.html`로 확인할 수 있다.

- url은 다음과 같다.

  ```python
  app_name = "movies"
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('<int:movie_pk>/', views.detail, name="detail"),
      path('<int:movie_pk>/review/', views.create_review, name="create_review"),
      path('<int:movie_pk>/review/delete/<int:review_pk>/', views.delete_review, name="delete_review"),
      path('<int:movie_pk>/like/', views.like, name='like'),
      path('<int:movie_pk>/score/<int:score>/', views.create_score, name='create_score'),
      path('search/', views.search, name='search'),
  ]
  ```

  

- 이 앱을 통해 만든 모델은 다음과 같다.

  ```python
  class Genre(models.Model):
      name = models.CharField(max_length=20)
      
      def __str__(self):
          return self.name
  
  class Movie(models.Model):
      title = models.CharField(max_length=50)
      open_date = models.CharField(max_length=20)
      description = models.TextField()
      audi_score = models.IntegerField()
      net_score = models.IntegerField()
      press_score = models.IntegerField()
      audi = models.IntegerField()
      rate = models.CharField(max_length=20)
      naver_code = models.CharField(max_length=20)
      poster = models.TextField()
      youtube_score = models.FloatField()
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", blank=True)
      genre = models.ManyToManyField(Genre, related_name="genre_movies")
      watched_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="watched_movie", blank=True)
  
      class Meta:
          ordering = ('-youtube_score', )
  
      def __str__(self):
          return self.title
  
  class Video(models.Model):
      channelId = models.TextField()
      channelTitle = models.TextField()
      videoTitle = models.TextField()
      description = models.TextField()
      videoId = models.TextField()
      created_at = models.TextField()
      thumbnail_small = models.TextField()
      thumbnail_medium = models.TextField()
      thumbnail_high = models.TextField()
      view_count = models.IntegerField()
      like_count = models.IntegerField()
      dislike_count = models.IntegerField()
      comment_count = models.IntegerField()
      video_src = models.TextField()
      iframe = models.TextField()
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  
      def __str__(self):
          return self.videoTitle
  
  class Movie_Score(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
      score = models.FloatField()
      objects = DataFrameManager()
  ```

  - 각각의 모델은 장르, 영화, 비디오, 점수에 해당한다. 비디오 테이블은 대부분 TextField로 만들었는데 이는 heroku의 데이터베이스를 고려한 결정이었다. 웹에서 데이터를 가져오다보니 그 길이가 지나치게 길어질 수 있기에 CharField를 100 이상으로 설정하였더니, 길이가 100을 넘어가면 heroku 데이터베이스에서 에러가 발생하였다. 그렇기에 이를 방지하고자 String 타입의 데이터는 전부 TextField로 저장하였다.
  - Movie_score 필드는 사용자의 영화에 대한 평점을 의미한다. 유저가 상세 페이지에서 특정 영화에 평점을 부여한다면 그 기록이 이 테이블에 반영된다.

