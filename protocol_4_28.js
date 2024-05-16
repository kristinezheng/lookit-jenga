function generateProtocol() {
    let allsequences = [
        //["IMG_7972.mp4", "IMG_8321.mp4", "IMG_8890.mp4"],
        //["IMG_7973.mp4", "IMG_7982.mp4", "IMG_8866.mp4"],
        //["IMG_7974.mp4", "IMG_7993.mp4", "IMG_8886.mp4"],
        //["IMG_7978.mp4", "IMG_8305.mp4", "IMG_8889.mp4"],
        //["IMG_7979.mp4", "IMG_8315.mp4", "IMG_8895.mp4"]

        ["IMG_8317.mp4", "IMG_8321.mp4", "IMG_8890.mp4"],
        ["IMG_8320.mp4", "IMG_7982.mp4", "IMG_8866.mp4"],
        ["IMG_7974.mp4", "IMG_7993.mp4", "IMG_8886.mp4"],
        ["IMG_7978.mp4", "IMG_8873.mp4", "IMG_8889.mp4"],
        ["IMG_7979.mp4", "IMG_8315.mp4", "IMG_8895.mp4"]

    ]

    let frames = {
        "instructions": {
            "kind": "exp-lookit-instructions",
            "blocks": [{
                    "image": {
                        "alt": "Jenga blocks",
                        "src": "https://myblocks.s3.us-east-2.amazonaws.com/intro_example.png",
                        "width": 100
                    }
                },
                {
                    "title": "Welcome!",
                    "listblocks": [{
                        "text": "Welcome to playing with block towers! In this study, we are looking at when children develop intuitions about the stability of stacked blocks and whether their emotional expressions as a tower is being built correlate with actual changes in the tower’s stability. Please follow the instructions below to participate."
                    }]
                },
                {
                    "title": "Instructions",
                    "listblocks": [{
                        "text": "In this study, your child will be shown three short videos of block stacking. We will ask your child to watch the video and will record your child’s reactions to the videos to see what they attend to and react to."
                    }]
                },
                {
                    "title": "Requirements",
                    "listblocks": [{
                            "text":  "Please note you will need a laptop or desktop computer (not a mobile device) running Chrome or Firefox to participate."
                        },
                        {
                            "text": "A quiet and comfortable space for you and your child."
                        }
                    ]
                }
            ],
            "nextButtonText": "Let's Get Started!"
        },
        "instructions-2": {
            "kind": "exp-lookit-instructions",
            "blocks": [{
                    "title": "Let's Get Started!",
                    "listblocks": [{
                        "text": "We will now start the experiment! After you click 'Begin', your computer will take a moment to activate the camera for video recording. You will then see the first block tower movie. The movie will start playing automatically. All your child needs to do is watch the movie. When the movie is over, you can hit the “Next” button to watch the next movie. There are three movies in total."
                    }]
                },
                {
                    "image": {
                        "src": "https://s3.amazonaws.com/9.85-jenga-towers-2/instructions-image.png",
                        "alt": "Example of the demo."
                    }
                }
            ],
            "nextButtonText": "Begin"
        },
        "video-config": {
            "kind": "exp-video-config",
            "troubleshootingIntro": "If you're having any trouble getting your webcam set up, please feel free to call Aaron, the graduate student researcher for this project, at (123) 456-7890 and we'd be glad to help you out!"
        },
        "start-recording-with-video": {
            "kind": "exp-lookit-start-recording",
            "baseDir": "https://www.mit.edu/~kimscott/placeholderstimuli/",
            "videoTypes": [
                "webm",
                "mp4"
            ],
            "video": "attentiongrabber",
            "displayFullscreen": true,
            "waitForVideoMessage": " "
        },
        "stop-recording-with-video": {
            "kind": "exp-lookit-stop-recording",
            "baseDir": "https://www.mit.edu/~kimscott/placeholderstimuli/",
            "videoTypes": [
                "webm",
                "mp4"
            ],
            "video": "attentiongrabber",
            "displayFullscreen": true,
            "waitForUploadMessage": " "
        },
        "video-consent": {
            "gdpr": false,
            "kind": "exp-lookit-video-consent",
            "template": "consent_002",
            "PIName": "Laura Schulz",
            "institution": "Massachusetts Institute of Technology",
            "purpose": "We are interested in whether both adults and children understand the complex dynamics involved in changing physical events. We are looking at whether we can decode subtle changes in children’s emotional expressions as they watch block towers being built. If so, we might be able to get a continuous measure of children’s changing expectations about the stability of the tower and see whether children’s intuitive physics is sensitive to dynamic changes in events.",
            "procedures": "First you will review some instructions, and get set up for the study. During the study, your child can sit anywhere where they can comfortably see the screen. They will see three movies of block towers being built. We will ask your child to watch the video and will record your child’s reactions to the videos to see what they attend to and react to. There are no expected risks from taking part in this study.",
            "payment": "After you finish the study, we will email you an Amazon gift card within three days. We pay $15/hour prorated for the length of the study with a minimum payment of $5/study. We anticipate that this study will take ten minutes to complete so you will receive a $5 gift card. ",
            "research_rights_statement": "This research has been reviewed and approved by an Institutional Review Board (“IRB”), a group of people who oversee research involving humans as participants. Information to help you understand research is on-line at https://templatestudiesinstitute.edu/irb. You may talk to a IRB staff member at (123) 456-7890 or IRBAdmin@tsi.edu for any of the following: 1) Your questions, concerns, or complaints are not being answered by the research team; 2) you cannot reach the research team; 3) you want to talk to someone besides the research team; 4) you have questions about your rights as a research subject; 5) you want to get information or provide input about this research.",
            "PIContact": "Laura Schulz (contact: lschulz@mit.edu)"
        },
        "positioning-config": {
            "kind": "exp-video-config-quality",
            "title": "It's time to get your child & get in position!",
            "introText": "",
            "showRecordMenu": false,
            "requireTestVideo": false,
            "completedItemText": "Got it!",
            "instructionBlocks": [{
                    "title": "Center your webcam if needed",
                    "text": "<strong>Make sure the webcam you're using is roughly centered</strong> relative to this monitor. This makes it much easier for us to tell whether your child is looking to the left or right!",
                    "image": {
                        "src": "https://raw.githubusercontent.com/lookit/template-study-stim/master/tetris/img/centering.png",
                        "alt": "Example images of using centered external webcam on monitor or built-in webcam on laptop."
                    }
                },
                {
                    "title": "Make sure you can clearly see your child's face",
                    "text": "Take a few moments to get settled and make sure your child's face is clearly visible in the webcam preview to the right. You may need to adjust the webcam angle or turn on a light to make sure his or her eyes are visible."
                },
                {
                    "text": "The green button down below will start the study. Press the button once you and your child are ready to go!",
                    "title": "When you're ready, press the green button and close your eyes"
                }
            ],
            "requireItemConfirmation": true,
            "recordingInstructionText": ""
        },
        "my-exit-survey": {
            "kind": "exp-lookit-exit-survey",
            "debriefing": {
                "text": "<b>Purpose</b> <br> Thank you for participating in our experiment! This might seem like a very simple task: just watching movies of block towers being built. However, your child is helping us learn something important: whether children’s emotional expressions correlate with changes in the stability of these block towers. <br><br><b>Experimental Design</b> <br> We showed your child three short movies of blocks being stacked one by one. Your child’s facial expressions and body language was recorded as they watched the movies. We expect that children may react with a subtle change in their emotional expressions to certain moments in the videos when the block tower becomes unstable. However, we might be wrong! Your child may have no particular reaction to our movies or no reaction that correlates with our predictions. In our studies, the children are always correct; their responses tell us if, when, and how our methods and ideas need to change. <br><br><b>Why this matters</b><br>The physical properties of events involve many complex dynamics. We are interested in children’s sensitivity to these complex changes. We can’t easily ask young children to give us a rating of a tower’s stability on a 0-100 scale at each time point as the tower is being built but we think we might be able to use children’s natural reactions (e.g., increasing suspense or anticipation) to get a continuous measure of their changing expectations about the towers’ stability. We can then see if children’s responses correlate with models of the actual physics and changing stability of these towers – and if children’s expectations about these events change with age and experience. This study might give us insight into the development of our intuitions about  objects and forces and help us understand more about how children learn about the physical world. Thank you so much for participating in our study! Research on child development would not be possible without your support! <br><br>",
                "image": {
                    "src": "https://myblocks.s3.us-east-2.amazonaws.com/example_image.png",
                    "alt": "video screenshots"
                },
                "title": "Thank you for participating in our study!"
            }
        },
        "study-completion": {
            "kind": "exp-lookit-video",
            "video": {
                "width": 100,
                "loop": true,
                "source": "ThankYouMovie"
            },
            "requiredDuration": 5,
            "requireAudioCount": 0,
            "requireVideoCount": 0,
            "doRecording": true,
            "baseDir": "https://raw.githubusercontent.com/lookit/template-study-stim/master/tetris/",
            "videoTypes": [
                "mp4"
            ],
            "backgroundColor": "white",
            "autoProceed": true,
            "restartAfterPause": true,
            "pauseKey": " ",
            "pauseKeyDescription": "X",
            "pauseAudio": "pause",
            "pauseVideo": "Elmo",
            "pauseText": "",
            "unpauseAudio": "return_after_pause"
        }

    }

    // function shuffle(array) {
    //     // https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array 
    //     let currentIndex = array.length;

    //     // While there remain elements to shuffle...
    //     while (currentIndex !== 0) {

    //       // Pick a remaining element...
    //       let randomIndex = Math.floor(Math.random() * currentIndex);
    //       currentIndex--;

    //       // And swap it with the current element.
    //       [array[currentIndex], array[randomIndex]] = [
    //         array[randomIndex], array[currentIndex]];
    //     }
    //     return array;
    //   }

    /* Randomize array in-place using Durstenfeld shuffle algorithm */
    function shuffleArray(array) {
        let arrayCopy = array.slice();
        for (var i = arrayCopy.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var temp = arrayCopy[i];
            arrayCopy[i] = arrayCopy[j];
            arrayCopy[j] = temp;
        }
        return arrayCopy; // Return the shuffled copy
    }


    let selectedSequenceIndex = Math.floor(Math.random() * allsequences.length);
    let basedir = "https://myblocks.s3.us-east-2.amazonaws.com/"
    console.log(selectedSequenceIndex)
    console.log(allsequences[selectedSequenceIndex])
    // let video1_source = basedir.concat(allsequences[selectedSequenceIndex][0])
    // let video2_source = basedir.concat(allsequences[selectedSequenceIndex][1])
    // let video3_source = basedir.concat(allsequences[selectedSequenceIndex][2])

    let permuted_sequence = shuffleArray(allsequences[selectedSequenceIndex])
    console.log("shuffled")
    console.log(permuted_sequence)

    let video1_source = basedir.concat(permuted_sequence[0])
    let video2_source = basedir.concat(permuted_sequence[1])
    let video3_source = basedir.concat(permuted_sequence[2])

    // // let btrials = {
    //     "sampler": "permute",
    //     "kind": "choice",
    //     "id": "block-video",
    //     "commonFrameProperties": {
    //         "showPreviousButton": false,
    //         "kind": "exp-lookit-video",
    //         "parentTextBlock": {
    //             "text": "Watch the video!"
    //         },
    //         "backgroundColor": "white",
    //         "requiredDuration": 0,
    //         "requireVideoCount": 0,
    //         "doRecording": true,
    //         "autoProceed": true,
    //         "restartAfterPause": true,
    //         "nextButtonEnabled": false
    //     },
    //     "frameOptions": [{
    //             "video": {
    //                 "width": 100,
    //                 "loop": false,
    //                 "source": [{
    //                     "src": video1_source,
    //                     "type": "video/mp4"
    //                 }]
    //             }
    //         },
    //         {
    //             "video": {
    //                 "width": 100,
    //                 "loop": false,
    //                 "source": [{
    //                     "src": video2_source,
    //                     "type": "video/mp4"
    //                 }]
    //             }
    //         },
    //         {
    //             "video": {
    //                 "width": 100,
    //                 "loop": false,
    //                 "source": [{
    //                     "src": video3_source,
    //                     "type": "video/mp4"
    //                 }]
    //             }
    //         }

    //     ]

    // }
    // frames["block-trials"] = btrials;
    // console.log(btrials)

    let bt1 = {

        "id": "block-video1",
        "kind": "exp-lookit-video",
        "video": {
            "width": 100,
            "loop": false,
            "source": [{
                "src": video1_source,
                "type": "video/mp4"
            }]
        },

        "showPreviousButton": false,

        "parentTextBlock": {
            "text": "Watch video #1!"
        },
        //"showProgressBar": true,
        "backgroundColor": "white",
        "doRecording": true,
        "autoProceed": false,
        "restartAfterPause": false,
        "nextButtonEnabled": true,

        "basedir": "https://myblocks.s3.us-east-2.amazonaws.com/",
        "videoTypes": [
            "mp4"
        ]
    }


    let bt2 = {

        "id": "block-video1",
        "kind": "exp-lookit-video",
        "video": {
            "width": 100,
            "loop": false,
            "source": [{
                "src": video2_source,
                "type": "video/mp4"
            }]
        },

        "showPreviousButton": false,

        "parentTextBlock": {
            "text": "Watch video #2!"
        },
        "backgroundColor": "white",
        "doRecording": true,
        "autoProceed": false,
        "restartAfterPause": false,
        "nextButtonEnabled": true,

        "basedir": "https://myblocks.s3.us-east-2.amazonaws.com/",
        "videoTypes": [
            "mp4"
        ]
    }


    let bt3 = {

        "id": "block-video1",
        "kind": "exp-lookit-video",
        "video": {
            "width": 100,
            "loop": false,
            "source": [{
                "src": video3_source,
                "type": "video/mp4"
            }]
        },

        "showPreviousButton": false,

        "parentTextBlock": {
            "text": "Watch video #3!"
        },
        //"showProgressBar": true,
        "backgroundColor": "white",
        "doRecording": true,
        "autoProceed": false,
        "restartAfterPause": false,
        "nextButtonEnabled": true,

        "basedir": "https://myblocks.s3.us-east-2.amazonaws.com/",
        "videoTypes": [
            "mp4"
        ]
    }

    frames["block-trials1"] = bt1;
    frames["block-trials2"] = bt2;
    frames["block-trials3"] = bt3;

    let t = {
        "kind": "exp-lookit-video",
        "videoTypes": [
            "mp4"
        ],
        "video": {
            "top": 5,
            "left": 0,
            "width": 100,
            "loop": false,
            "source": [{
                "src": video2_source,

                "type": "video/mp4"
            }]
        },
        "backgroundColor": "white",
        "autoProceed": false,
        "doRecording": false,
        "requiredDuration": 0,
        "requiredVideoCount": 1
    }

    frames["test"] = t;

    // console.log(frames["block-trials1"]);

    let sequences = [
        "instructions",
        "video-config",
        "video-consent",
        "positioning-config",
        "instructions-2",
        "start-recording-with-video",
        "block-trials1",
        "block-trials2",
        "block-trials3",
        "stop-recording-with-video",
        "study-completion",
        "my-exit-survey"
    ]

    return {
        frames: frames,
        sequence: sequences
    };
}