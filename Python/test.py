# -*- coding: utf-8 -*-
from summarize import NewSummarize


list_of_news = [
	
	'''A leader of the Jammu Kashmir Peoples Democratic Party has made a shocking statement, a day after the Central government amended several laws and allowed people from across the country to buy land in the union territory of Jammu and Kashmir. Surinder Chaudhary, PDP leader and close associate of party chief Mehbooba Mufti, caused outrage with his remarks when he suggested that rapes will increase in Jammu and Kashmir if Indians from rest of the country come to settle here after changes in land laws. “Jammu has a rich Dogra culture and legacy; we have given sacrifices for the country. We are not saying they (outsiders) will start coming crimes like rapes as soon as they come to settle here. What we are saying is also being said by Assam and Maharashtra etc, that people should not come from outside as they will snatch jobs,” Chaudhary told Times Now. “Today, the Jammu region is very peaceful. Here, women come from different villages to study in Jammu. You can see as to what happened in Faridabad, where a girl was shot dead, and also what happened in Hathras,” he added. “Rape cases are increasing. All this is being shown on national TV,” the PDP leader went on to add.''',
	'''Voting was held in 71 assembly seats of Bihar in the first phase of three-phase elections amid tight security and COVID-19 guidelines in place. Prime Minister Narendra Modi urged people in Bihar to participate in the festival of democracy, while following coronavirus safety guidelines, including maintaining social distancing and wearing a mask. More than two crore voters in the state will decide the future of 1,066 candidates, including former chief minister and Hindustani Awam Morcha chief Jitan Ram Manjhi, and eight ministers of the Nitish Kumar cabinet is at stake. The key candidates whose fate is at stake include eight state ministers - Dr Prem Kumar, Krishnanandan Verma, Shailesh Kumar, Jai Kumar Singh, Santosh Kumar Nirala, Ramnarayan Mandal, Vijay Kumar Sinha, and Brijkishore Bind. Other prominent candidates who are in the fray in this phase are ace shooter Shreyasi Singh from Jamui seat, Manjhi and former speaker Uday Narayan Chaudhary from Imamganj, Shatrughan Sinha’s son Luv Sinha from Bankipur and Bahubali Anant Kumar Singh from Mokama constituency.''',
	'''In yet another blow to Indian professionals with an American dream, the Trump administration has now proposed to scrap the computerised lottery system to grant H-1B work visas to foreign technology professionals and replace it with a wage-level-based selection process. The move is expected to counter the downward pressure on the wages of US workers. The Department of Homeland Security (DHS) said on Wednesday that a notification on the new system is being published in the Federal Register on Thursday. Stakeholders are required to respond to the notification within 30 days. In a release, DHS stated, "The Department of Homeland Security (DHS) has announced the transmission to the Federal Register of a notice of proposed rulemaking (NPRM) that would prioritize the selection of H-1B registrations (or petitions, if the registration process is suspended) based on corresponding wage levels in order to better protect the economic interests of U.S. workers, while still allowing U.S. employers to meet their personnel needs and remain globally competitive."DHS said that modifying the H-1B cap selection process by replacing the random selection process with a wage-level-based selection process is a better way to allocate H-1Bs when demand exceeds supply. If finalized as proposed, this new selection process would incentivize employers to offer higher wages or petition for positions requiring higher skills and higher-skilled workers instead of using the program to fill relatively lower-paid vacancies. “With this proposed rule, the Trump administration is continuing to deliver on its promise to protect the American worker while strengthening the economy. The H-1B program is often exploited and abused by U.S. employers, and their U.S. clients, primarily seeking to hire foreign workers and pay lower wages,” said Acting DHS Deputy Secretary Ken Cuccinelli. “The current use of random selection to allocate H-1B visas makes it harder for businesses to plan their hiring, fails to leverage the H-1B program to truly compete for the world’s best and brightest, and hurts American workers by bringing in relatively lower-paid foreign labor at the expense of the American workforce," he added. This effort would affect H-1B registrations submitted by prospective petitioners seeking to file H-1B cap-subject petitions. The proposal would be implemented for both the H-1B regular cap and the H-1B advanced degree exemption, but would not change the order of selection between the two as established by the H-1B registration requirement final rule. DHS will open a public comment period once the NPRM is published in the Federal Register. Interested parties will have 30 days to submit comments relevant to the proposed rule and 60 days to submit comments relevant to the proposed information collection. The Department will review all properly submitted comments, consider them and draft responses before issuing a final rule.'''
]


f = open("result.txt", "a")

for item in list_of_news:
	news = NewSummarize(item)
	f.write(news.summarize() + '\n')

f.close()