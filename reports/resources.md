# Список статей и ссылок

## Статьи
* Uplift Prediction with Dependent Feature Representation in Imbalanced Treatment and Control Conditions [сборник статей, 47 с.](https://link.springer.com/content/pdf/10.1007%2F978-3-030-04221-9.pdf)
  - Датасеты
    - Hillstorm
    - Criterio
  - Модели
    - Dependent Data Representation (DDR)
    - Shared Data Representation (SDR)
    - Two Model
    - Revert Label - используется замена переменных таргета

* Uplift modeling for clinical trial data [статья](http://people.cs.pitt.edu/~milos/icml_clinicaldata_2012/Papers/Oral_Jaroszewitz_ICML_Clinical_2012.pdf) - Несмотря на то, что данная статья не из ритейла, в ней раскрываются проблемы использования малых данных (вроде, точно не проверял, но видел в других статьях, что обычно медицинских данных на порядкИ меньше, чем ритейла). Также, статья написана в более академическом стиле, по сравнению с другими ритейловыми.

* Decision Trees for Uplift Modeling [[презентация](https://www.researchgate.net/publication/220765228_Decision_Trees_for_Uplift_Modeling), [статья](https://link.springer.com/content/pdf/10.1007/s10115-011-0434-0.pdf)] - в статье используются медицинские датасеты (листинг можно найти в статье). Из особенностей можно отметить Uplift в случае нескольких treatment'ов, подробное описание подходов, тоерем, лемм, доказательств, выводов.

* Machine learning methods for estimating heterogeneouscausal effects [статья](https://www.researchgate.net/publication/274644919_Machine_Learning_Methods_for_Estimating_Heterogeneous_Causal_Effects)- вводят некоторые методы валидации результатов (что-то похожее на CV, но со спецификой Uplift)
  - Модели
    - Замена переменных для приведения задачи к задаче регрессии
    - и др. Tree based (5 моделей, 4 пункт)
  - Датасет
    - Датасет поисковой выдачи (вроде как закрытый)

* Machine Learning Estimation of Heterogeneous Treatment Effects with Instruments, [статья](https://arxiv.org/pdf/1905.10176.pdf) - что-то свежее, и однозначно следует почитать

* Metalearners for estimating heterogeneous treatment effects using machine learning, [статья](https://www.pnas.org/content/116/10/4156) - тоже стоит почитать

* Deep IV: A Flexible Approach for Counterfactual Prediction [[статья (52 цит.)](http://proceedings.mlr.press/v70/hartford17a/hartford17a.pdf), [github](https://github.com/jhartford/DeepIV)] - что-то очень интересное, можно почитать, но не в первую очередь

## Блоги
* [Criterio uplift dataset exploration](https://s3.us-east-2.amazonaws.com/criteo-uplift-dataset/large-scale-benchmark.pdf) - Ноутбук с пошаговым объяснением статьи по используемому [датасету](https://s3.us-east-2.amazonaws.com/criteo-uplift-dataset/large-scale-benchmark.pdf)

* Uplift Modeling Blog (20.09.2018) [ссылка](https://humboldt-wi.github.io/blog/research/theses/uplift_modeling_blogpost/) - довольно развёрнутое объяснение дизайна эксперимента и проверки результата обучения. Однако есть один большой минус - код написан на ***R***

* [Jupyter notebook](https://nbviewer.jupyter.org/github/maks-sh/scikit-uplift/blob/master/notebooks/RetailHero.ipynb) с примерами использования scikit-uplift. Ноутбук, наверное, является логическим продолжением первой статьи от МТСа по Uplift моделированию.

* Обзор методов Uplift моделирования от МТС на habr\`е ([1 часть](https://habr.com/ru/company/ru_mts/blog/485980/), [2 часть](https://habr.com/ru/company/ru_mts/blog/485976/))

## Видео
* Рассылка персональных сообщений физ лицам клиентам банка — Александр Фонарев ([видео](https://www.youtube.com/watch?v=UNegf9Rgpnw))

* Валерий Бабушкин: Аплифт моделирование ([youtube](https://www.youtube.com/watch?v=yFQAIJBYXI0))

## Соревнования
* [X5 Retail Hero](https://retailhero.ai/video) - соревнование, одним из треков которого было предсказание uplift

## Датасеты
В хронологическом порядке:
* Hillstorm dataset, 2008 г. [[описание данных](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html), [данные](www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv)] - 64000 пользователей, 1/3 которых были разосланы e-mail с "Mens merchandise", 1/3 с "Woman merchandise" и 1/3 не было ничего разослано. Один из самых используемы датасетов для валидации алгоритмов.

* Criterio [[описание данных](http://cail.criteo.com/criteo-uplift-prediction-dataset/), [un-biased данные](https://s3.us-east-2.amazonaws.com/criteo-uplift-dataset/criteo-uplift-v2.csv.gz), [paper](https://s3.us-east-2.amazonaws.com/criteo-uplift-dataset/large-scale-benchmark.pdf)] - Не синтетический, но анонимизированный, вплоть до величин, датасет. На 2018 год ялвялся самым большим открытым, не синтетическим датасетом.

* X5 Retail Hero, [[dataset](локально), [видео](https://retailhero.ai/video)] - пока сложно что-либо сказать, так как не нашёл ссылки на само соревнование. Плюс надо его поисследовать.

## Проекты

* Microsoft ALICE [репозиторий](https://github.com/microsoft/EconML) - куча примеров различных алгоритмов

* Uber CausalML [github](https://github.com/uber/causalml) - множество алгоритмов, реализовнных на питоне - модно - молодёжно

* wayfair PyLift [github](https://github.com/wayfair/pylift) - что-то старое и менее популярное, чем предыдущее решение.

* scikit-uplift [github](https://github.com/maks-sh/scikit-uplift) - видел в каком-то блоге
