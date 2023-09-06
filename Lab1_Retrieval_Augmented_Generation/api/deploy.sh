# Build the function.zip file for a Lambda function.
# 1. Package all the dependencies as listed in requirements.txt.
# 2. Special handling for numpy as we need the version that works on Amazon Linux.
# 3. Remove boto3 to reduce the size of the package (uncompressed < 250MB) as it is already included in the Lambda runtime.
# 4. pip install with the --no-cache-dir option to reduce the size of the package.

# all dependencies used by the lambda are installed in the deps folder
DEPS_DIR=deps

# useful constants 
FN_ZIP_FILE=function.zip
REQS_TXT_PATH=app/requirements.txt
APP_DIR=app
APP_NAME=llm-analytics-apps-workshop

# derive bucket name to put the function.zip in, to be used if the caller did not provide a bucket name
ACCOUNT_ID=`aws sts get-caller-identity --output text --query 'Account'`
REGION=`aws ec2 describe-availability-zones --output text --query 'AvailabilityZones[0].[RegionName]'`
FN_BUCKET_NAME=sagemaker-$REGION-$ACCOUNT_ID

if [ -z "$1" ]
then
  echo "bucket name from $FN_ZIP_FILE not provided as input, going with the default $FN_BUCKET_NAME"
  fn_bucket=$FN_BUCKET_NAME
else
  echo "bucket name provided as $1, going to use that for uploading $FN_ZIP_FILE"
  fn_bucket=$1
fi

# remove any existing depenencies dir or function.zip to start fresh
echo going to remove $DEPS_DIR and $FN_ZIP_FILE
rm -rf $DEPS_DIR
rm -f $FN_ZIP_FILE

# get all the dependencies in a dir
echo going to pip install dependencies listed in $REQS_TXT_PATH
pip install -r $REQS_TXT_PATH --no-cache-dir --target=$DEPS_DIR
echo done installing dependencies

# remove boto3, it is is already included in the lambda python runtime
cd $DEPS_DIR
rm -rf boto*
echo deleted boto 

# zip up the dependencies
echo going to package dependencies in $FN_ZIP_FILE
rm -rf `find . -name .ipynb_checkpoints`
zip -r9 ../$FN_ZIP_FILE .
cd -

# add the app files (Lambda code) to the zip file
echo going to package $APP_DIR in $FN_ZIP_FILE
zip -g ./$FN_ZIP_FILE -r $APP_DIR

# upload the function.zip to s3 so that it is available for a Lambda deployment
echo going to upload $FN_ZIP_FILE to $fn_bucket
ls -ltr $FN_ZIP_FILE 
aws s3 cp $FN_ZIP_FILE s3://$fn_bucket/$APP_NAME/

echo "all done"
