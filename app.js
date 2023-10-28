const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/Project5703', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(async () => {
  console.log('Connected to MongoDB');
  await checkTrialCollection(); // scan after connection
})
.catch(error => {
  console.error('Connection error:', error);
  process.exit(1); // exit
});

const Schema = mongoose.Schema;

// Experiment Schema
const ExperimentSchema = new Schema({
  Experiment_ID: {
    type: String,
    required: false,
    unique: false
  },
  name: {
    type: String,
    required: false,
    unique: false
  },
  metadata: {
    type: String,
    required: false,
    unique: false
  },
  DOI: {
    type: Number,
    required: false,
    unique: false
  }
});

// use colleciton in the database
const Experiment = mongoose.model('Experiment', ExperimentSchema, 'Experiment');

// Trial Schema
const TrialSchema = new Schema({
  Trail_ID: {
    type: String,
    required: false,
    unique: false
  },
  Experiment_ID: {
    type: String,
    required: false,
    unique: false
  },
  Description: {
    type: String,
    required: false,
    unique: false
  }
  
});

// use the collection
const Trial = mongoose.model('Trial', TrialSchema, 'Trial');

async function checkTrialCollection() {
  const trials = await Trial.find({}); // 获取所有 Trial 文档

  for (const trial of trials) {
    const experimentExists = await Experiment.findOne({ Experiment_ID: trial.Experiment_ID });
    if (!experimentExists) {
      console.error('Error: Experiment not found for Trial. Document:', trial);
      await Trial.deleteOne({ _id: trial._id });
      process.exit(1);
    }
  }

  console.log('Trial collection check completed.');
  process.exit(0); // exit 
}
