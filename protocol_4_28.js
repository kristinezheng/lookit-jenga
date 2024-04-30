function generateProtocol() {
    let allsequences = [
        ["IMG_7972.mp4", "IMG_8321.mp4", "IMG_8890.mp4"],
        ["IMG_7973.mp4", "IMG_7982.mp4", "IMG_8866.mp4"],
        ["IMG_7974.mp4", "IMG_7993.mp4", "IMG_8886.mp4"],
        ["IMG_7978.mp4", "IMG_8305.mp4", "IMG_8889.mp4"],
        ["IMG_7979.mp4", "IMG_8315.mp4", "IMG_8895.mp4"]
    ]

    let frames = {
        "instructions": {
            "kind": "exp-lookit-instructions",
            "blocks": [{
                    "image": {
                        "alt": "Jenga blocks",
                        "src": "https://i0.wp.com/awarddesign.com/wp-content/uploads/2019/05/619UhnrOfAL.jpg?fit=689%2C1300&ssl=1",
                        "width": 100
                    }
                },
                {
                    "title": "Welcome!",
                    "listblocks": [{
                        "text": "Welcome to “Jenga” block stacking! This exciting study aims to understand when children develop the ability to predict stability of stacked blocks. Follow the instructions below to participate."
                    }]
                },
                {
                    "title": "Instructions",
                    "listblocks": [{
                        "text": "In this study, your child will be shown a series of videos stacking blocks one by one."
                    }]
                },
                {
                    "title": "Requirements",
                    "listblocks": [{
                            "text": "A computer or tablet with a stable internet connection."
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
                        "text": "We will now start the experiment! Upon clicking 'Begin', your computer will take a moment to activate the camera for video recording and then proceed to display the video. The video will start playing automatically, and your child should focus on watching the video."
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
        "video-consent": {
            "gdpr": false,
            "kind": "exp-lookit-video-consent",
            "template": "consent_002",
            "PIName": "Laura Schulz",
            "institution": "Massachusetts Institute of Technology",
            "purpose": "This experiment is a project from the 9.85 course offered at the Massachusetts Institute of Technology. This project aims to investigate when children begin to develop intuitive reasoning about physical phenomena, particularly focusing on their ability to predict the stability of multi-layer block towers. By participating in this study, you're contributing valuable insights into the timeline of cognitive development in early childhood. The observations made during this experiment will provide researchers with critical information on the emergence of intuitive physics reasoning and whether infants can anticipate the stability of complex structures. Thank you for being a part of this exciting exploration into the cognitive development of our little ones!",
            "procedures": "First you will review some instructions, and get set up for the study. This questionnaire helps us interpret babies’ behavior in the main task. During the study, your child will sit on your lap or in an appropriate chair if you choose. On the screen, there will be blocks that are slowly stacking on top of each other. We ask your child to click a button when they believe the tower will fall. We will also record how long your child looks at each block to learn about what information they notice and pay attention to. There are no expected risks from taking part in this study.",
            "payment": "Within about 3 days after participating in this study, we will email you a $7 'Tango card' gift card which you can exchange for credit at a variety of stores. To be eligible for the gift card, your child must be in the age range for this study, you need to submit a valid consent statement, and we need to see that there is a child with you. But we will send a gift card even if you do not finish the whole study or if we are not able to use your child's data. There are no other direct benefits to you or others from taking part in this research.",
            "research_rights_statement": "This research has been reviewed and approved by an Institutional Review Board (“IRB”), a group of people who oversee research involving humans as participants. Information to help you understand research is on-line at https://templatestudiesinstitute.edu/irb. You may talk to a IRB staff member at (123) 456-7890 or IRBAdmin@tsi.edu for any of the following: 1) Your questions, concerns, or complaints are not being answered by the research team; 2) you cannot reach the research team; 3) you want to talk to someone besides the research team; 4) you have questions about your rights as a research subject; 5) you want to get information or provide input about this research.",
            "PIContact": "Kristine Zheng (kxzheng@mit.edu), Haoran Wen (hranwen@mit.edu)"
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
                "text": "One way scientists discover how babies develop and learn--and how humans think in general--is to ask what's in the child brain's \"toolbox\" and what’s learned from experience. In this study, we asked whether children can already mentally reason about physics, such as gravity. In order to understand and use the objects in their environment, babies need to know - or figure out - how objects interact with each other when stacked or balance. We tested this by recording how your child looked at and reasoned about videos of “Jenga” like tower stacking, with blocks being placed one by one on each other with no, little, or some offset. They were asked to click the ‘Next’ button when they believed the tower would fall.  Above is a picture from all the videos that your child saw during the study. Your child’s pattern of looking and decision about the towers falling helps to answer the question of whether stability reasoning is a is a core, built-in ability or something that is learned through experience. That in turn can inform how active a role your child plays in their own learning!<br><br>Thank you for participating in our study! Within three days, once we confirm your consent video, we will email you a $7 Tango gift card which you can exchange for credit at a variety of stores. If you have any questions, please don’t hesitate to contact us at kxzheng@mit.edu & hranwen@mit.edu! <br><br>",
                "image": {
                    "src": "https://s3.amazonaws.com/9.85-jenga-towers-2/video+screenshots+1.png",
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
            "text": "Watch the video!"
        },
        "backgroundColor": "white",
        "doRecording": true,
        "autoProceed": false,
        "restartAfterPause": true,
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
            "text": "Watch the video!"
        },
        "backgroundColor": "white",
        "doRecording": true,
        "autoProceed": false,
        "restartAfterPause": true,
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
            "text": "Watch the video!"
        },
        "backgroundColor": "white",
        "doRecording": true,
        "autoProceed": false,
        "restartAfterPause": true,
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
        // "video-consent",
        // "positioning-config",
        // "instructions-2",
        "block-trials1",
        "block-trials2",
        "block-trials3",
        // "study-completion",
        // "my-exit-survey"
    ]

    return {
        frames: frames,
        sequence: sequences
    };
}
