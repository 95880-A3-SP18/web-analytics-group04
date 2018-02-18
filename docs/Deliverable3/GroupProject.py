
# coding: utf-8

# ## Scrape Reviews from Amazon
# ## Group04: Rui Yang, Chen Wei, Shuaijun Ye
# 



from bs4 import BeautifulSoup
import csv


# #### Step 1. Find the Overall Score for the Products


average_star_soup = BeautifulSoup(open('amazon/AverageStar.html'), "html.parser")
# The part of average star
average_star_dic = {}

average_star_block = average_star_soup.find('div', attrs = {'class':'a-fixed-left-grid AverageCustomerReviews'})
average_star = average_star_block.find('div', attrs = {'class': 'a-fixed-left-grid-col a-col-left'}).get_text()
review_counts = average_star_block.find('div', attrs = {'class': 'a-fixed-left-grid-col a-col-right'}).get_text()

average_star_dic.update({'Average Star': average_star})
average_star_dic.update({'Total Review': review_counts})

# The percentage of each star
histogram_block = average_star_soup.find('table', attrs = {'id': 'histogramTable'})
star_percentage = [histogram_block.find('tr', attrs = {'data-reftag': ('cm_cr_arp_d_hist_'+ str(i))}).get_text() for i in range(1,6)]
for star in star_percentage:
    star = star.replace('star','')
    average_star_dic.update({star.split(' ')[0]:star.split(' ')[1]})

# Write the content into csv
with open('AverageStar.csv','w', newline = '\n') as file:
    writer = csv.writer(file, delimiter=',')
    for key,value in average_star_dic.items():
        writer.writerow([key, value])


# #### Step 2. Find Reviews in Each Star & Save Them 

# In[80]:


# format of star_level: 'OneStarReviews'
def get_reviews(star_level, page_number):
    
    outfile = open('%s.csv' %star_level, 'w', newline = '\n')
    writer = csv.writer(outfile, delimiter=',')
    
    for i in range(1, page_number + 1):
        file = 'amazon/sourcePages/' + star_level + '-%s.html'%i
        star_soup = BeautifulSoup(open(file), "html.parser")
        review_block = star_soup.find_all('div', attrs = {'class': 'a-section review'})
        for block in review_block:
            color = block.find('a', attrs = {'class': 'a-size-mini a-link-normal a-color-secondary'}).get_text()
            review = block.find('span', attrs = {'class': 'a-size-base review-text'}).get_text()
            writer.writerow([color.split(': ')[-1], str(review)])
    
    outfile.close()


# Get the reviews, store them in separate csv file
get_reviews('OneStarReviews', 36)
get_reviews('TwoStarReviews', 30)
get_reviews('ThreeStarReviews', 36)
get_reviews('FourStarReviews', 70)
get_reviews('FiveStarReviews', 324)

