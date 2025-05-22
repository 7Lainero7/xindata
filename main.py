from appdir.functions import download_kaggle_csv, drop_freelancer_id


download_kaggle_csv('shohinurpervezshohan/freelancer-earnings-and-job-trends', 'freelancer_earnings_bd.csv', './data')
drop_freelancer_id('data/freelancer_earnings_bd.csv')


