{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import seaborn as sns\n",
    "\n",
    "\n",
    " \n",
    "data = pd.read_csv(\"kyphosis.csv\") \n",
    " \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Kyphosis</th>\n",
       "      <th>Age</th>\n",
       "      <th>Number</th>\n",
       "      <th>Start</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>absent</td>\n",
       "      <td>71</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>absent</td>\n",
       "      <td>158</td>\n",
       "      <td>3</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>present</td>\n",
       "      <td>128</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>absent</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>absent</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Kyphosis  Age  Number  Start\n",
       "0   absent   71       3      5\n",
       "1   absent  158       3     14\n",
       "2  present  128       4      5\n",
       "3   absent    2       5      1\n",
       "4   absent    1       4     15"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x983a4e0>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 540x540 with 12 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier\n",
    "from sklearn.model_selection import train_test_split # Import train_test_split function\n",
    "from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "feature_cols = [\"Age\",\"Number\",\"Start\"]\n",
    "X = data[feature_cols] # Features\n",
    "y = data.Kyphosis # Target variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create Decision Tree classifer object\n",
    "clf = DecisionTreeClassifier()\n",
    "\n",
    "# Train Decision Tree Classifer\n",
    "clf = clf.fit(X_train,y_train)\n",
    "\n",
    "#Predict the response for test dataset\n",
    "y_pred = clf.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.68\n"
     ]
    }
   ],
   "source": [
    "print(\"Accuracy:\",metrics.accuracy_score(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
