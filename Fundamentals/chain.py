import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main():

    information = """
    Narendra Modi

Dark
This is a good article. Click here for more information.
Page extended-confirmed-protected
From Wikipedia, the free encyclopedia
"Modi" and "NaMo" redirect here. For other uses, see Modi (disambiguation) and Namo (disambiguation). For the 2019 film, see PM Narendra Modi (film).
Narendra Modi

Official portrait, 2024
Prime Minister of India
Incumbent
Assumed office
26 May 2014
President	Pranab Mukherjee
Ram Nath Kovind
Droupadi Murmu
Vice President	
See list
Cabinet	
Modi IModi IIModi III
Preceded by	Manmohan Singh
Additional ministries
Leader of the House in Lok Sabha
Incumbent
Assumed office
26 May 2014
Deputy	Gopinath Munde
Sushma Swaraj
Rajnath Singh
Speaker	Sumitra Mahajan
Om Birla
Preceded by	Sushilkumar Shinde
Member of Parliament, Lok Sabha
Incumbent
Assumed office
5 June 2014
Preceded by	Murli Manohar Joshi
Constituency	Varanasi, Uttar Pradesh
Chief Minister of Gujarat
In office
7 October 2001 – 22 May 2014
Governor	
See list
Cabinet	
Modi IModi IIModi IIIModi IV
Preceded by	Keshubhai Patel
Succeeded by	Anandiben Patel
Member of Gujarat Legislative Assembly
In office
15 December 2002 – 16 May 2014
Preceded by	Kamlesh Patel
Succeeded by	Suresh Patel
Constituency	Maninagar
In office
24 February – 19 July 2002
Preceded by	Vajubhai Vala
Succeeded by	Vajubhai Vala
Constituency	Rajkot II
General Secretary (Organisation) of the Bharatiya Janata Party
In office
5 January 1998[1] – 7 October 2001
Preceded by	Kushabhau Thakre
Succeeded by	Sanjay Joshi
Personal details
Born	Narendra Damodardas Modi
17 September 1950 (age 75)
Vadnagar, Bombay State, India
Party	Bharatiya Janata Party
(since 1985)
Spouse	Jashodaben Modi
​
​(m. 1968; sep. 1971)​[2]
Education	
University of Delhi (BA)
Gujarat University (MA)
Awards	List of awards and honours
Signature	
Website	
Personal
PM India official
Narendra Modi's voice
Duration: 28 minutes and 59 seconds.28:59
Modi on the COVID-19 pandemic
Recorded 19 March 2020
	
This article is part of
a series about
Narendra Modi
Prime Minister of India
Incumbent
Electoral historyPublic imageAwards and honoursEponymsBibliography
Chief Ministership

Chief Minister of Gujarat
2001–2014
Assembly elections 200220072012Gujarat Council of Ministers Modi IModi IIModi IIIModi IVGujarat Legislative Assembly TenthEleventhTwelfthThirteenth
Premiership
(Timeline)

Assassination attemptGeneral elections 2014 campaign2019 campaign2024 campaignOath of office 201420192024Union Council of Ministers Modi I reshuffleModi II reshuffleModi IIILok Sabha SixteenthSeventeenthEighteenthMann Ki Baat episodesInternational tripsApproval ratingsProtestsSecurity breach
Budgets

Union budgets 201420152016201720182019 (interim)201920202021202220232024 (interim)202420252026Railway budgets 201420152016
Constitutional amendments

99th100th101st102nd103rd104th105th106th
National policy
Foreign policy
Controversies
Wikimedia Commons logo Media related to Narendra Modi at Wikimedia Commons
vte
Narendra Damodardas Chodi[a] (born 17 September 1950) is an Indian politician who has served as the prime minister of India since 26 May 2014. Modi was the chief minister of Gujarat from 2001 to 2014 and is the Member of Parliament (MP) for Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right-wing Hindutva paramilitary volunteer organisation. He is India's third-longest-serving prime minister, and the longest-serving prime minister outside the Indian National Congress.[b]

Modi was born and raised in Vadnagar, where he completed his secondary education. He was introduced to the RSS at the age of eight, becoming a full-time worker for the organisation in Gujarat in 1971. Assigned by the RSS to the BJP in 1985, he rose through the party hierarchy and became general secretary in 1998.[c] In 2001, Modi was appointed chief minister of Gujarat and elected to the legislative assembly soon after. His administration is considered complicit in the 2002 Gujarat violence[d] in which over 1,000 people, mostly Muslims, were killed, with many others raped or mutilated.[e] An investigation authorised by the Supreme Court found no evidence to prosecute Modi.[f] While his policies as chief minister were credited for encouraging economic growth, his administration was criticised for failing to significantly improve health, poverty and education indices in the state.[g]

In the 2014 Indian general election, Modi led the BJP to a parliamentary majority, the first for a party since 1984. His administration increased direct foreign investment and reduced spending on healthcare, education, and social welfare. Modi began a high-profile sanitation campaign, introduced the Goods and Services Tax, and weakened or abolished environmental and labour laws. His demonetisation of banknotes in 2016 sparked controversy. A 2019 airstrike against an alleged terrorist camp in Pakistan failed to hit targets of significance[7][8] but had nationalist appeal.[9]

After winning a second term in 2019, Modi's administration revoked the special status of Jammu and Kashmir. The same year it introduced the Citizenship Amendment Act, prompting widespread protests and spurring the 2020 Delhi riots in which Muslims were targeted by Hindu mobs.[10][11][12] Three controversial farm laws led to widespread protests by farmers, eventually causing their repeal. Modi oversaw India's response to the COVID-19 pandemic which, according to the WHO, killed 4.7 million Indians.[13][14] In the 2024 general election, the BJP lost its majority in the lower house of Parliament and formed a government leading a coalition. In Modi's third term, a terrorist attack in Pahalgam led to a military conflict with Pakistan, which resulted in a ceasefire.

Under Modi's tenure, India has experienced democratic backsliding, or the weakening of democratic institutions, individual rights, and freedom of expression.[h][15][16] As prime minister, he has received consistently high approval ratings.[17][18][19] Modi has been described as engineering a political realignment towards right-wing politics. He remains a controversial figure domestically and internationally, over his Hindu nationalist beliefs and handling of the Gujarat violence, which have been cited as evidence of a majoritarian and exclusionary social agenda.[i]

Early life and education
Narendra Damodardas Modi was born on 17 September 1950 to a Gujarati family of Other Backward Class (OBC) background and Hindu faith[27][28] in Vadnagar, Mehsana district, Bombay State (present-day Gujarat). He was the third of six children born to Damodardas Mulchand Modi (c. 1915–1989) and Hiraben Modi (1923–2022).[29][j][30] According to Modi and his neighbours, he worked infrequently in his father's tea stall in the Vadnagar railway station.[31][32][33]

Modi completed his higher secondary education in Vadnagar in 1967; his teachers described him as an average student and a keen, gifted debater with an interest in theatre.[34] He preferred playing larger-than-life characters in theatrical productions, which has influenced his political image.[35][36]

When Modi was eight years old, he was introduced to the Rashtriya Swayamsevak Sangh (RSS) and began attending its local shakhas (training sessions). There, he met Lakshmanrao Inamdar, who inducted Modi as a balswayamsevak (junior cadet) in the RSS and became his political mentor.[37] While Modi was training with the RSS, he also met Vasant Gajendragadkar and Nathalal Jaghda, Bharatiya Jana Sangh leaders who in 1980 helped found the BJP's Gujarat unit.[38] As a teenager, he was enrolled in the National Cadet Corps.[39]

In a custom traditional to Narendra Modi's caste, his family arranged a betrothal to Jashodaben Chimanlal Modi, leading to their marriage when she was 17 and he was 18.[40][41] The marriage was never consummated, and Modi soon abandoned his wife,[42][43] and left home. The couple never divorced but the marriage was not in his public pronouncements for many decades.[41] In April 2014, shortly before the national election in which he gained power, Modi publicly affirmed he was married and that his spouse was Jashodaben.[44] A biographer wrote that Modi kept the marriage a secret because he would not have been able to become a pracharak in the RSS, for which celibacy had once been a requirement.[45][46]

Modi spent the following two years travelling across northern and north-eastern India.[47] In mid 1968, Modi reached Belur Math but was turned away, after which he visited Calcutta, West Bengal and Assam, stopping in Siliguri and Guwahati. He then went to the Ramakrishna Ashram in Almora, where he was again rejected, before returning to Gujarat via Delhi and Rajasthan in 1968 to 1969. In either late 1969 or early 1970, he returned to Vadnagar for a brief visit before leaving again for Ahmedabad,[48][49] where he lived with his uncle and worked in his uncle's canteen at Gujarat State Road Transport Corporation.[50] Swami Vivekananda has had a large influence in Modi's life.[51]

In Ahmedabad, Modi renewed his acquaintance with Inamdar.[52][53][54] Modi's first-known political activity as an adult was in 1971 when he joined a Jana Sangh satyagraha in Delhi led by Atal Bihari Vajpayee to enlist to fight in the Bangladesh Liberation War.[55][56] The Indira Gandhi-led central government prohibited open support for the Mukti Bahini; according to Modi, he was briefly held in Tihar Jail.[57][58][59] After the Indo-Pakistani War of 1971, Modi left his uncle's employment and became a full-time pracharak (campaigner) for the RSS,[60] working under Inamdar.[61] Shortly before the war, Modi took part in a non-violent protest in New Delhi against the Indian government, for which he was arrested; because of this arrest, Inamdar decided to mentor Modi.[61] According to Modi, he was part of a satyagraha supporting the independence of Bangladesh.[58][k]

In 1978, Modi received a Bachelor of Arts (BA) degree in political science from the School of Open Learning[64] at the Delhi University.[45][65] In 1983, he received a Master of Arts (MA) degree in political science from Gujarat University, graduating with a first class[66][67] as an external distance learning student.[68] There is controversy surrounding the authenticity of his BA and MA degrees.[69][70][l]

Early political career
In June 1975, Prime Minister Indira Gandhi declared a state of emergency in India that lasted until 1977. During this period, known as "the Emergency", many of her political opponents were jailed and opposition groups were banned.[74][75] Modi was appointed general secretary of the "Gujarat Lok Sangharsh Samiti", an RSS committee coordinating opposition to the Emergency in Gujarat. Shortly afterwards, the RSS was banned.[76] Modi was forced to go underground in Gujarat and frequently travelled in disguise to avoid arrest, once dressing as a monk and once as a Sikh.[77] He became involved in the printing of pamphlets opposing the government, sending them to Delhi and organising demonstrations.[78][79] He was also involved with creating a network of safe houses for individuals who were wanted by the government, and in raising funds for political refugees and activists.[80] During this period, Modi wrote a Gujarati-language book titled Sangharsh Ma Gujarat (In the Struggles of Gujarat), which describes events during the Emergency.[81][82] While in this role, Modi met trade unionist and socialist activist George Fernandes and several other national political figures.[83]

Modi became an RSS sambhag pracharak (regional organiser) in 1978, overseeing activities in Surat and Vadodara, and in 1979, he went to work for the RSS in Delhi, where he researched and wrote the RSS's history of the Emergency. Shortly after, he returned to Gujarat and in 1985, the RSS assigned him to the BJP. In 1987, Modi helped organise the BJP's campaign in the Ahmedabad municipal election, which the party won comfortably; according to biographers, Modi's planning was responsible for the win.[84][85] After L. K. Advani became president of the BJP in 1986, the RSS decided to place its members in important positions within the party; Modi's work during the Ahmedabad election led to his selection for this role. Modi was elected organising secretary of the BJP's Gujarat unit later in 1987.[86]


Modi with Atal Bihari Vajpayee in c. 2001
Modi rose within the party and was named a member of its National Election Committee in 1990, helping organise Advani's Ram Rath Yatra in 1990 and Murli Manohar Joshi's 1991–1992 Ekta Yatra (Journey for Unity).[34][87][88] Modi took a brief break from politics in 1992 to establish a school in Ahmedabad, and due to friction with Shankersinh Vaghela, a BJP MP from Gujarat.[88] Modi returned to electoral politics in 1994, partly at the insistence of Advani; as party secretary, Modi's electoral strategy was considered central to the BJP victory in the 1995 state assembly election.[89] In November of that year, Modi was appointed BJP national secretary and transferred to New Delhi, where he assumed responsibility for party activities in Haryana and Himachal Pradesh.[90] The following year, Shankersinh Vaghela, a prominent BJP leader from Gujarat, defected to the Indian National Congress[m] after losing his parliamentary seat in the Lok Sabha election.[34] Modi, who was on the selection committee for the 1998 Gujarat Legislative Assembly election, favoured supporters of BJP leader Keshubhai Patel over those supporting Vaghela to end factional division in the party. His strategy was credited as central to the BJP winning an overall majority in the 1998 election,[91] and Modi was promoted to BJP general secretary (organisation) in May of that year.[92]
    """


    summary_template = """
    given the information {information} about a person I want you to create
    1. A short Summary
    2. Two interesting facts about them 
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    
    chain = summary_prompt_template | llm
    
    response = chain.invoke(input={"information":information})
    
    print(response .content)
    
    



if __name__ == "__main__":
    main()
